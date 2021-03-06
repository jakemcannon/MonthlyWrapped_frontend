import config

import boto3

bucket_name = config.bucket_name
local_file_name = 'test_from_local2.jpg'
remote_s3_file_name = 'test.jpg'

client = boto3.client('s3', aws_access_key_id = config.api_key, aws_secret_access_key = config.api_secret)

def upload(file_name, bucket, object_name):

	response = client.upload_file(file_name, bucket, object_name)
	return response


def download(bucket, file_name):
	print(file_name)
	print(f'./{file_name}')
	response = client.download_file(bucket_name, file_name, f'./media/{file_name}')
	return response


# upload(local_file_name, bucket_name, local_file_name)
download(bucket_name, remote_s3_file_name)



