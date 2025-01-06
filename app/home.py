from flask import Blueprint, render_template

home = Blueprint('home', __name__)

@home.route('/')
def index():
    # Poți adăuga logica pentru extragerea datelor despre utilizator
    return render_template('home.html', user_name="User")
