import logging
import config

import requests
import urllib
import json	
from flask import Flask, abort, request, redirect, session, url_for

from db import db
from db import User

auth_endpoint = config.sp_auth_endpoint
token_endpoint = config.sp_token_endpoint
client_id = config.sp_client_id
client_secret = config.sp_client_secret
redirect_uri = config.sp_redirect_uri
scope =  config.sp_scope

db_filename = "monthlywrapped.db"

app = Flask(__name__)
app.config['SECRET_KEY'] = config.flask_secret_key

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_filename}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
	db.create_all()


@app.route("/")
@app.route("/home")
def home():
	return {"data": "Home page"}


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
	print(auth_code)
	# return token
	return redirect(url_for('authenticate', auth_code=auth_code))

@app.route("/auth/<auth_code>")
def authenticate(auth_code):
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

	# <--------------------------------- error occurs here ---------------------------------> 
	print(token_resp.json())
	print("<--------------------------------- error occurs here --------------------------------->")

	# get user page
	headers = {'Authorization': f"Bearer {token_resp.json()['access_token']}"}
	user_resp = requests.get('https://api.spotify.com/v1/me', headers=headers)
	user_data = user_resp.json()
	print(user_data)

	user = User.query.filter_by(user_id=user_data['id']).first()
	if not user:
		print("Creating our new user in the db")
		print(user)
		new_user = User(
			user_id=user_data['id'],
			access_token=session['user_info']['access_token'],
			refresh_token=session['user_info']['refresh_token']
		)
		db.session.add(new_user)
		db.session.commit()

	verified_user = User.query.filter_by().first()
	print(verified_user)


	# this all works correctly until I got to refresh.
	# refreshing pings the Spotify OAuth2 endpoint again, which changes the acess_code
	# The access code is then different from what I have in the db
	# So when I try to refresh it

	return verified_user.serialize()
if __name__ == '__main__':
    app.run(debug=True)



