import boto3
from flask import Flask, current_app, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity


from .test_named_tuple import make_api_request
from .story import SongStory
from .story import ArtistStory

from models import db
from models import User

app = current_app

@app.route("/generate_images")
@jwt_required()
def get_end_of_month_images():

	# fetch the current user
	user = get_jwt_identity()
	# TODO: throw exception if no users found
	u = User.query.filter_by(user_id=user['user_id']).first()

	# build those two images
	# TODO: throw exception if api response is bad
	response = make_api_request(u.access_token)

	s = SongStory(response[0].artists, response[0].songs, response[0].images).create_image()
	a = ArtistStory(response[1].artists, response[1].images).create_image()
	# a.create_image()
	# s.create_image()

	# upload those two images to S3

	# retrieve links for those two images

	# return those two images


	return "hello world from the generate_images route"