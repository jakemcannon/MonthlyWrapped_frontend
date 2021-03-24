from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    access_token = db.Column(db.String, nullable=False)
    refresh_token = db.Column(db.String, nullable=False)


    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id', '')
        self.access_token = kwargs.get('access_token', '')
        self.refresh_token = kwargs.get('refresh_token')

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
        }

