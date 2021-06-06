import boto3
from flask import Flask, current_app, jsonify
from flask_jwt_extended import jwt_required

app = current_app

@app.route("/generate_images")
def get_end_of_month_images():

	# fetch the current user
	user = get_jwt_identity()
	# TODO: throw exception if no users found
	u = User.query.filter_by(user_id=user['user_id']).first()

	# build those two images

	# upload those two images to S3

	# retrieve links for those two images

	# return those two images


	return "hello world from the generate_images route"