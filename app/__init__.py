from flask import Flask
from .models import db

def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'your_secret_key_here'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emotinest.db'

	# Inițializează baza de date
	db.init_app(app)

	# Înregistrează blueprint-urile
	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint, url_prefix='/auth')

	from .home import home as home_blueprint
	app.register_blueprint(home_blueprint)

	from .forms import forms as forms_blueprint
	app.register_blueprint(forms_blueprint)

	return app
