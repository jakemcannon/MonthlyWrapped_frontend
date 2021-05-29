

import boto3
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, jwt_required

import config


app = Flask(__name__)
app.config['SECRET_KEY'] = config.flask_secret_key

bucket_name = config.bucket_name

client = boto3.client('s3', aws_access_key_id = config.api_key, aws_secret_access_key = config.api_secret)

jwt = JWTManager(app)


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