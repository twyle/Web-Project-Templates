from ...extensions.extensions import db, ma
from datetime import datetime
from flask_login import UserMixin
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', email='{self.email}', image_file='{self.image_file}')"


class OAuth(OAuthConsumerMixin, db.Model):
    """This class stores the user authentication information.

    Attributes
    ----------
    user_id: str
        The unique user identifier, same as the User.id
    user: User
        The user found in the users table

    """

    user_id: int = db.Column(db.Integer, db.ForeignKey(User.id))
    user: User = db.relationship(User)