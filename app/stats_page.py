import config

import boto3
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

bucket_name = config.bucket_name
local_file_name = 'test_from_local2.jpg'

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'

CORS(app)

client = boto3.client('s3', aws_access_key_id = config.api_key, aws_secret_access_key = config.api_secret)

def get_signed_url(bucket_name, file_name, exp_seconds):
	return client.generate_presigned_url(
		ClientMethod='get_object',
		Params={
			'Bucket': bucket_name,
			'Key': file_name,
            'ResponseExpires': exp_seconds,
        })


if __name__ == '__main__':
    app.run(debug=True)
