from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Goal, DailyEntry
from sqlalchemy import func

home = Blueprint('home', __name__)

@home.route('/')
def index():
    # Fetch user goals
    user_goals = Goal.query.filter_by(user_id=1).all()  # Înlocuiește 1 cu utilizatorul conectat
    goals = [goal.description for goal in user_goals]

    # Statistici
    total_entries = db.session.query(func.count(DailyEntry.id)).scalar() or 0
    avg_stress = db.session.query(func.avg(DailyEntry.stress_level)).scalar() or 0
    avg_sleep = db.session.query(func.avg(DailyEntry.sleep_quality)).scalar() or 0

    return render_template('home.html', user_name="User", total_entries=total_entries, goals=goals, avg_stress=avg_stress, avg_sleep=avg_sleep)

@home.route('/add_goal', methods=['POST'])
def add_goal():
    goal_description = request.form.get('goal')
    if goal_description:
        new_goal = Goal(description=goal_description, user_id=1)  # Înlocuiește user_id=1 cu utilizatorul conectat
        db.session.add(new_goal)
        db.session.commit()
        flash("Goal added successfully!", category='success')
    else:
        flash("Goal cannot be empty!", category='error')

    return redirect(url_for('home.index'))
