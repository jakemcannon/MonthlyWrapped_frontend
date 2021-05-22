from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    spotify_id = db.Column(db.Integer, nullable=False)
    access_token = db.Column(db.String, nullable=False)
    refresh_token = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=True)


    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id', '')
        self.spotify_id = kwargs.get('spotify_id')
        self.access_token = kwargs.get('access_token', '')
        self.refresh_token = kwargs.get('refresh_token')
        self.email = kwargs.get('email')

    def serialize(self):
        return {
            'id': self.id,
            'spotify_id': self.spotify_id,
            'user_id': self.user_id,
            'email': self.email
        }

