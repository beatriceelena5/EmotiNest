from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Păstrăm doar baza de date
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Cheia secretă e bună de păstrat pentru sesiuni/flash messages
    app.config['SECRET_KEY'] = 'ppc_energy_secret_key'
    
    # Putem schimba numele bazei de date în ceva relevant pentru tematică
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///energy_data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Importăm și înregistrăm doar blueprint-urile de care avem nevoie
    from .home import home as home_blueprint
    from .statistics import statistics as statistics_blueprint

    app.register_blueprint(home_blueprint)
    app.register_blueprint(statistics_blueprint)

    # Creăm tabelele automat dacă nu există (util pentru prima rulare în Docker)
    with app.app_context():
        db.create_all()

    return app