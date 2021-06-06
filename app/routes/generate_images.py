import datetime

import boto3
from flask import Flask, current_app, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity


from .test_named_tuple import make_api_request
from .story import SongStory
from .story import ArtistStory

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

def get_current_end_of_month_stories():

	# TODO / Look into
	# Do we need to iterate over every image for a given year
	# can we not query for the cur_month given we know the naming scheme (which is a WIP atm)
	
	urls = []
	try:

		for item in client.list_objects(Bucket=bucket_name, Prefix = f'user1/songs/{today.year}/')['Contents']:

			key = item['Key']
			cur_month = key[17:19]
			if key[17:19] == "13":
				urls.append({"song": get_signed_url(bucket_name, key, 60)})
				print("yay")

		for item in client.list_objects(Bucket=bucket_name, Prefix = f'user1/artists/{today.year}')['Contents']:
			key = item['Key']
			cur_month = key[19:21]
			if key[19:21] == "13":
				print("yay")
				urls.append({"artist": get_signed_url(bucket_name, key, 60)})

	except KeyError:
		pass

	return urls



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
	# TODO:
	# - Determine where local images are being saved on disk
	# - Update name and path parameter to be not hard coded
	# - Upload to correct yearly folder based on cur year
	# - Come up with naming scheme for key in s3 - ? something to do with months?
	# - look into ImageGrid frontend to recall how ordering out of s3 is working
	upload_to_s3("song_story_test.jpg", f"user1/songs/{today.year}/" + "13.jpg")
	upload_to_s3("artist_story_test.jpg", f"user1/artists/{today.year}/" + "13.jpg")
	get_current_end_of_month_stories()

	# retrieve links for those two images
	results = get_current_end_of_month_stories()

	return jsonify(results)
