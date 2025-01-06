from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class DailyEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emotional_state = db.Column(db.String(50), nullable=False)
    stress_level = db.Column(db.Integer, nullable=False)
    sleep_quality = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime, default=db.func.current_timestamp())

