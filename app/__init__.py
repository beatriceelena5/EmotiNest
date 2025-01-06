from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
	from .models import User
	return User.query.get(int(user_id))  # Găsește utilizatorul după ID

def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'your_secret_key_here'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emotinest.db'

	# Inițializează extensiile
	db.init_app(app)
	login_manager.init_app(app)

	# Configurează ruta implicită pentru login
	login_manager.login_view = 'auth.login'
	login_manager.login_message = "Please log in to access this page."
	login_manager.login_message_category = "info"

	# Înregistrează blueprint-urile
	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint, url_prefix='/auth')

	from .home import home as home_blueprint
	app.register_blueprint(home_blueprint)

	from .forms import forms as forms_blueprint
	app.register_blueprint(forms_blueprint)

	from .statistics import statistics as statistics_blueprint
	app.register_blueprint(statistics_blueprint)

	return app
