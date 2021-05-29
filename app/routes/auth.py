
import uuid
import requests

import urllib

from flask import Flask, current_app, request, redirect
from flask_cors import CORS, cross_origin
from flask_jwt_extended import create_access_token

from models import db
from models import User

app = current_app

# spotify config variables
client_id = current_app.config["SP_CLIENT_ID"]
client_secret = current_app.config["SP_CLIENT_SECRET"]
auth_endpoint = current_app.config["SP_AUTH_ENDPOINT"]
token_endpoint = current_app.config["SP_TOKEN_ENDPOINT"]
scope = current_app.config["SP_SCOPE"]
redirect_uri = current_app.config["SP_REDIRECT_URI"]

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

	user =  User.query.filter_by(spotify_id=user_data['id']).first()

	if not user:
		print("Creating our new user in the db")
		print(user)
		user_id = str(uuid.uuid4())
		new_user = User(
			user_id=user_id,
			spotify_id = user_data['id'],
			access_token=token_resp.json()['access_token'],
			refresh_token=token_resp.json()['refresh_token']
		)
		db.session.add(new_user)
		db.session.commit()

	user = User.query.filter_by().first()
	jwt_access_token = create_access_token(identity={"user_id":user.user_id, "email": user.email})

	query_param = "?token=" + jwt_access_token
	return redirect("http://localhost:3000/cred" + query_param, code=302)

if __name__ == '__main__':
    app.run(debug=True)