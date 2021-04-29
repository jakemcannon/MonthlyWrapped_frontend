import logging
import config

from functools import wraps

import uuid
import requests
import urllib
import json	

import boto3
from flask import Flask, abort, request, redirect, session, url_for, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_cors import CORS, cross_origin

from db import db
from db import User
import jwt

auth_endpoint = config.sp_auth_endpoint
token_endpoint = config.sp_token_endpoint
client_id = config.sp_client_id
client_secret = config.sp_client_secret
redirect_uri = config.sp_redirect_uri
scope =  config.sp_scope
bucket_name = config.bucket_name

db_filename = "monthlywrapped.db"

app = Flask(__name__)
app.config['SECRET_KEY'] = config.flask_secret_key

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_filename}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
	db.create_all()

jwt = JWTManager(app)
CORS(app)

client = boto3.client('s3', aws_access_key_id = config.api_key, aws_secret_access_key = config.api_secret)

# ----------- This toy example works based off the following tutorial -----------
# https://www.youtube.com/watch?v=AsQ8OcVvK3U&ab_channel=Vuka

# @app.route("/test_register", methods=['POST'])
# def test_register():
# 	user_id = 1234
# 	access_token = create_access_token(identity={"user_id":user_id})
# 	return {"access_token": access_token}, 200

# @app.route("/test_login")
# def test_login():
# 	access_token = create_access_token(identity={"user_id":user_id})
# 	return {"access_token": access_token}, 200


# @app.route("/test_secret", methods=['GET'])
# @jwt_required()
# def test_secret():
# 	user = get_jwt_identity()
# 	print(user)
# 	return "secret route", 200

 # ------------------------------------------------------------------

@app.route("/login", methods=["GET", "POST"])
def create_authorization_url():
	payload = {
		'client_id':client_id, 
		'response_type':'code', 
		'redirect_uri': redirect_uri, 
		'scope': scope,
		}
	auth_url = auth_endpoint + urllib.parse.urlencode(payload)
	return {"data": auth_url}
	# return redirect(auth_url, code=200)

@app.route("/callback")
def callback():
	auth_code = request.args.get("code")
	# return token

	post_data = {
		"grant_type": "authorization_code", 
		"code": auth_code, "redirect_uri": redirect_uri, 
		"client_id": client_id, 
		"client_secret": client_secret
	}

	headers = {
		'Authorization': 'Basic ', 
		'Content-type':'application/x-www-form-urlencoded', 
		'Accept':'application/json'
	}
	token_resp = requests.post(token_endpoint, auth=(client_id, client_secret), data=post_data, headers=headers)

	# get user page to access access token and refresh token
	headers = {'Authorization': f"Bearer {token_resp.json()['access_token']}"}
	user_resp = requests.get('https://api.spotify.com/v1/me', headers=headers)
	user_data = user_resp.json()

	# add user to our database
	# ******* note that this is not exactly what we want to do
	'''
	NOTE THAT THIS IS NOT EXACTLY WHAT WE WANT TO DO
	
	Here we are checking if a user exits in db with the spotify_id
	Instead, we probably want to hide this and have our own id

	Additionally, we will get that id from the jwt token

	Even more, we probably, want a check on this auth route that the user hasn't already authenticated
	If they have, redirect them to the home page 

	'''

	# pull data out of jwt token, specifcally the user_id

	# TODO: Redirec if the user
	print(user_data['id'])
	# 
	user = User.query.filter_by(user_id=user_data['id']).first()
	print(user)
	if not user:
		print("Creating our new user in the db")
		print(user)
		# TODO replace user_id with a new uuid() user_id, NOT spotify user_id
		user_id = str(uuid.uuid4())
		new_user = User(
			user_id=user_id,
			access_token=token_resp.json()['access_token'],
			refresh_token=token_resp.json()['refresh_token']
		)
		db.session.add(new_user)
		db.session.commit()
	verified_user = User.query.filter_by().first()
	print(verified_user)

	jwt_access_token = create_access_token(identity={"user_id":user_id})


	# return redirect(url_for('authenticate', auth_code=auth_code))
	# return jsonify(jwt_access_token)
	query_param = "?token=" + jwt_access_token
	return redirect("http://localhost:3000/content" + query_param, code=302)


# create a user route and test that I can get user
# I want to recieve a jwt from the frontend
# I then want to grab the user_id from the db
# Now that I have the user, I want to grab their access_token
# Now that I have their access token I want to make a get request to https://api.spotify.com/v1/me with the access token as a heaader
# first test with postman
# then build light frontend, and test with frontend request
@app.route("/user")
@jwt_required()
@cross_origin()
def get_user():
	user = get_jwt_identity()

	u = User.query.filter_by(user_id=user['user_id']).first()

	return jsonify(u.serialize())

@app.route("/playlists")
@jwt_required()
def get_playlists():

	user = get_jwt_identity()
	print(user)

	# query the database for user
	u = User.query.filter_by(user_id=user['user_id']).first()
	print(u.access_token)

	# make request to playlists
	headers = {'Authorization': f"Bearer {u.access_token}", 'Accept':'application/json','Content-Type': 'application/json'}
	playlists_resp = requests.get('https://api.spotify.com/v1/me/playlists', headers=headers)
	return {"data": playlists_resp.json()}


# stats page routes

def get_signed_url(bucket_name, file_name, exp_seconds):
	return client.generate_presigned_url(
		ClientMethod='get_object',
		Params={
			'Bucket': bucket_name,
			'Key': file_name,
            'ResponseExpires': exp_seconds,
        })


@app.route("/songs")
@jwt_required()
def get_songs():

	result = []
	urls = []
	prev_year = None
	try:
		# this prefix will need to change to include user uuid
		for item in client.list_objects(Bucket=bucket_name, Prefix = 'user1/songs')['Contents']:
			key = item['Key']
			if key.endswith('.png'):

				# this slice will need to be updated when users switch to uuid
				year = str(key[12:16])

				# this is a gross solution
				if prev_year == None:
					prev_year = year

				if prev_year != year:
					result.insert(0, {"year": prev_year, "months": urls})
					prev_year = year
					urls = []
					urls.append({"month": get_signed_url(bucket_name, key, 60)})
				else:
					urls.append({"month": get_signed_url(bucket_name, key, 60)})

		result.insert(0, {"year": prev_year, "months": urls})
	except KeyError:
		pass

	return jsonify(result)

@app.route("/artists")
@jwt_required()
def get_artists():

	result = []
	urls = []
	prev_year = None
	try:
		# this prefix will need to change to include user uuid
		for item in client.list_objects(Bucket=bucket_name, Prefix = 'user1/artists')['Contents']:
			key = item['Key']
			if key.endswith('.png'):

				# this slice will need to be updated when users switch to uuid
				year = str(key[14:18])

				# this is a gross solution
				if prev_year == None:
					prev_year = year

				if prev_year != year:
					result.insert(0, {"year": prev_year, "months": urls})
					prev_year = year
					urls = []
					urls.append({"month": get_signed_url(bucket_name, key, 60)})
				else:
					urls.append({"month": get_signed_url(bucket_name, key, 60)})

		result.insert(0, {"year": prev_year, "months": urls})
	except KeyError:
		pass

	return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)



