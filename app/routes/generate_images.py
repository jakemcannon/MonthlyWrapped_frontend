import datetime

import boto3
from flask import Flask, current_app, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity


from test_named_tuple import make_api_request
from story import SongStory
from story import ArtistStory

from models import db
from models import User

api_key = current_app.config['AWS_API_KEY']
secret_key = current_app.config['AWS_API_SECRET_KEY']
bucket_name = current_app.config['AWS_BUCKET_NAME']

app = current_app
client = boto3.client('s3', aws_access_key_id = api_key, aws_secret_access_key = secret_key)

today = datetime.datetime.now()

def get_signed_url(bucket_name, file_name, exp_seconds):
	return client.generate_presigned_url(
		ClientMethod='get_object',
		Params={
			'Bucket': bucket_name,
			'Key': file_name,
            'ResponseExpires': exp_seconds,
        })

def upload_to_s3(file_name, object_name):
	response = client.upload_file(file_name, bucket_name, object_name)
	return response

def get_end_of_month_stories():

	urls = []

	# TODO: update user parameter, year, and name of cur month image
	cur_month_song_key = f'user1/songs/{today.year}/13.jpg'
	cur_month_artist_key = f'user1/artists/{today.year}/13.jpg'
	urls.append({"song": get_signed_url(bucket_name, cur_month_song_key, 60)})
	urls.append({"artist": get_signed_url(bucket_name, cur_month_artist_key, 60)})

	return urls



@app.route("/generate_images")
@jwt_required()
def create_end_of_month_images():

	# fetch the current user
	user = get_jwt_identity()
	# TODO: throw exception if no users found
	u = User.query.filter_by(user_id=user['user_id']).first()

	# TODO:
	# - check if cur month has already been created, if so, do not create a duplicate
	# - idk if this will be a db table value or checking s3 for cur month is none None

	# build those two images
	# TODO: throw exception if api response is bad
	response = make_api_request(u.access_token)

	s = SongStory(response[0].artists, response[0].songs, response[0].images).create_image()
	a = ArtistStory(response[1].artists, response[1].images).create_image()
	# a.create_image()
	# s.create_image()

	# upload those two images to S3
	# TODO:
	# - Determine where local images are being saved on disk
	# - Update name and path parameter to be not hard coded
	# - Upload to correct yearly folder based on cur year
	# - Come up with naming scheme for key in s3 - ? something to do with months?
	# - look into ImageGrid frontend to recall how ordering out of s3 is working
	upload_to_s3("song_story_test.jpg", f"user1/songs/{today.year}/" + "13.jpg")
	upload_to_s3("artist_story_test.jpg", f"user1/artists/{today.year}/" + "13.jpg")
	get_end_of_month_stories()

	# retrieve links for those two images
	results = get_end_of_month_stories()

	return jsonify(results)
