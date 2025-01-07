from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    name = db.Column(db.String(150), nullable=False) 

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class DailyEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emotional_state = db.Column(db.String(50), nullable=False)
    stress_level = db.Column(db.Integer, nullable=False)
    sleep_quality = db.Column(db.Integer, nullable=False)
    energy_level = db.Column(db.Integer, nullable=False)
    happiness_level = db.Column(db.Float, nullable=False)
    productivity_level = db.Column(db.Integer, nullable=False)
    water_intake = db.Column(db.Float, nullable=False)
    physical_exercise = db.Column(db.Boolean, nullable=False)
    meditation = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime, default=db.func.current_timestamp())
