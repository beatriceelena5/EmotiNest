from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, logout_user, current_user
from .models import Goal, db
from sqlalchemy import func
from .models import DailyEntry

home = Blueprint('home', __name__)

@home.route('/')
@login_required
def index():
    user_goals = Goal.query.filter_by(user_id=current_user.id).all()

    # Calculăm statisticile pentru utilizator
    total_entries = db.session.query(func.count(DailyEntry.id)).filter_by(user_id=current_user.id).scalar() or 0
    avg_stress = db.session.query(func.avg(DailyEntry.stress_level)).filter_by(user_id=current_user.id).scalar() or 0
    avg_sleep = db.session.query(func.avg(DailyEntry.sleep_quality)).filter_by(user_id=current_user.id).scalar() or 0
    avg_energy = db.session.query(func.avg(DailyEntry.energy_level)).filter_by(user_id=current_user.id).scalar() or 0
    avg_happiness = db.session.query(func.avg(DailyEntry.happiness_level)).filter_by(user_id=current_user.id).scalar() or 0
    avg_productivity = db.session.query(func.avg(DailyEntry.productivity_level)).filter_by(user_id=current_user.id).scalar() or 0
    avg_water_intake = db.session.query(func.avg(DailyEntry.water_intake)).filter_by(user_id=current_user.id).scalar() or 0
    total_exercise_days = db.session.query(func.sum(DailyEntry.physical_exercise)).filter_by(user_id=current_user.id).scalar() or 0
    total_meditation_days = db.session.query(func.sum(DailyEntry.meditation)).filter_by(user_id=current_user.id).scalar() or 0

    return render_template(
        'home.html',
        user_name=current_user.name,
        total_entries=total_entries,
        avg_stress=round(avg_stress, 2),
        avg_sleep=round(avg_sleep, 2),
        avg_energy=round(avg_energy, 2),
        avg_happiness=round(avg_happiness, 2),
        avg_productivity=round(avg_productivity, 2),
        avg_water_intake=round(avg_water_intake, 2),
        total_exercise_days=int(total_exercise_days),
        total_meditation_days=int(total_meditation_days),
        goals=user_goals
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

@home.route('/delete_goal/<int:goal_id>', methods=['POST'])
@login_required
def delete_goal(goal_id):
    goal = Goal.query.get(goal_id)
    if goal and goal.user_id == current_user.id:  # Verifică dacă goal-ul aparține utilizatorului curent
        db.session.delete(goal)
        db.session.commit()
        flash("Goal deleted successfully!", category='success')
    else:
        flash("Goal not found or unauthorized action.", category='error')
    
    return redirect(url_for('home.index'))

@home.route('/logout')
@login_required
def logout():
    # Log out the current user
    logout_user()
    flash("You have been logged out.", category='success')
    return redirect(url_for('auth.login'))

