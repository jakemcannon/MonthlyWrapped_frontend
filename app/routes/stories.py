import boto3
from flask import Flask, current_app, jsonify
from flask_jwt_extended import jwt_required

api_key = current_app.config["AWS_API_KEY"]
secret_key = current_app.config["AWS_API_SECRET_KEY"]
bucket_name = current_app.config["AWS_BUCKET_NAME"]

app = current_app
client = boto3.client("s3", aws_access_key_id=api_key, aws_secret_access_key=secret_key)


def get_signed_url(bucket_name, file_name, exp_seconds):
    return client.generate_presigned_url(
        ClientMethod="get_object",
        Params={
            "Bucket": bucket_name,
            "Key": file_name,
            "ResponseExpires": exp_seconds,
        },
    )


@app.route("/songs")
@jwt_required()
def get_songs():

    result = []
    urls = []
    prev_year = None
    try:
        # this prefix will need to change to include user uuid
        for item in client.list_objects(Bucket=bucket_name, Prefix="user1/songs")[
            "Contents"
        ]:
            key = item["Key"]
            if key.endswith(".png"):

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
        for item in client.list_objects(Bucket=bucket_name, Prefix="user1/artists")[
            "Contents"
        ]:
            key = item["Key"]
            if key.endswith(".png"):

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
