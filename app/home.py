from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Goal

home = Blueprint('home', _name_)

@home.route('/')
def index():
    # Exemplu: Fetch user goals from database (temporar hardcodate pentru test)
    user_goals = Goal.query.all()  # În realitate, vei filtra după utilizatorul conectat
    goals = [goal.description for goal in user_goals]
    
    return render_template('home.html', user_name="User", total_entries=5, goals=goals)

@home.route('/add_goal', methods=['POST'])
def add_goal():
    goal_description = request.form.get('goal')
    if goal_description:
        new_goal = Goal(description=goal_description, user_id=1)  # Schimbă user_id pentru utilizatorul conectat
        db.session.add(new_goal)
        db.session.commit()
        flash("Goal added successfully!", category='success')
    else:
        flash("Goal cannot be empty!", category='error')

    return redirect(url_for('home.index'))
