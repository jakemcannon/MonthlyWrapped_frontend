
import requests

from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
jwt = JWTManager(app)

@app.route("/email", methods=["POST"])
@jwt_required()
def set_email():

	user = get_jwt_identity()

	u = User.query.filter_by(user_id=user['user_id']).first()
	email = request.get_json()["email"]
	u.email = email
	db.session.commit()

	jwt_access_token = create_access_token(identity={"user_id":u.user_id, "email": u.email})

	return jsonify(jwt_access_token)


if __name__ == '__main__':
    app.run(debug=True)