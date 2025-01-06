from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, logout_user, current_user
from .models import Goal, db
from sqlalchemy import func

home = Blueprint('home', __name__)

@home.route('/')
@login_required
def index():
    user_goals = Goal.query.filter_by(user_id=current_user.id).all()
    goals = [goal.description for goal in user_goals]

    total_entries = db.session.query(func.count(Goal.id)).filter_by(user_id=current_user.id).scalar() or 0
    avg_stress = db.session.query(func.avg(Goal.id)).filter_by(user_id=current_user.id).scalar() or 0
    avg_sleep = db.session.query(func.avg(Goal.id)).filter_by(user_id=current_user.id).scalar() or 0

    return render_template(
        'home.html',
        user_name=current_user.email,
        total_entries=total_entries,
        goals=goals,
        avg_stress=avg_stress,
        avg_sleep=avg_sleep
    )

@home.route('/add_goal', methods=['POST'])
@login_required
def add_goal():
    goal_description = request.form.get('goal')
    if goal_description:
        new_goal = Goal(description=goal_description, user_id=current_user.id)
        db.session.add(new_goal)
        db.session.commit()
        flash("Goal added successfully!", category='success')
    else:
        flash("Goal cannot be empty!", category='error')
    
    return redirect(url_for('home.index'))

@home.route('/logout')
@login_required
def logout():
    # Deloghează utilizatorul
    logout_user()
    flash("You have been logged out.", category='success')
    return redirect(url_for('auth.login'))
