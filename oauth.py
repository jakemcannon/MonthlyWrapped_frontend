import logging
import config

import requests
import urllib
import json	
from flask import Flask, abort, request, redirect, session, url_for

auth_endpoint = config.sp_auth_endpoint
token_endpoint = config.sp_token_endpoint
client_id = config.sp_client_id
client_secret = config.sp_client_secret
redirect_uri = config.sp_redirect_uri
scope =  config.sp_scope

app = Flask(__name__)
app.config['SECRET_KEY'] = config.flask_secret_key

@app.route("/auth")
def create_authorization_url():
	payload = {'client_id':client_id, 
		'response_type':'code', 
		'redirect_uri': redirect_uri, 
		'scope': scope}
	auth_url = auth_endpoint + urllib.parse.urlencode(payload)
	return redirect(auth_url)

@app.route("/callback")
def callback():
	print("hey, I made it to the callback page")
	token = get_token(request.args.get("code"))
	# return token
	return redirect(url_for('get_profile'))


def get_token(auth_code):
	post_data = {"grant_type": "authorization_code", "code": auth_code, "redirect_uri": redirect_uri, "client_id": client_id, "client_secret": client_secret}
	headers = {'Authorization': 'Basic ', 'Content-type':'application/x-www-form-urlencoded', 'Accept':'application/json'}
	resp = requests.post(token_endpoint, auth=(client_id, client_secret), data=post_data, headers=headers)
	# print(resp)
	# print(resp.json())
	# print(type(resp))
	session['token'] = TOKEN
	return resp.json()

@app.route("/my_token")
def get_my_token():
	t = session['token']

	return t

@app.route("/profile")
def get_profile():

	## if error message, then redirect user to the oauth sign in page

	headers = {'Authorization': f"Bearer {session['token'].get('access_token')}"}
	res = requests.get('https://api.spotify.com/v1/me', headers=headers)
	res_data = res.json()

	return res_data

if __name__ == '__main__':
    app.run(debug=True)
