import config

import boto3
from flask import Flask

bucket_name = config.bucket_name
local_file_name = 'test_from_local2.jpg'

app = Flask(__name__)

client = boto3.client('s3', aws_access_key_id = config.api_key, aws_secret_access_key = config.api_secret)

@app.route("/stats")
def stats():
	urls = []
	try:
		for item in client.list_objects(Bucket=bucket_name, Prefix = 'user1/')['Contents']:
			url = get_signed_url(config.bucket_name, item['Key'], 60)
			urls.append(url)
	except KeyError:
		pass
	return {"data":content}



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
