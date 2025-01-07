from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import db, DailyEntry
from sqlalchemy.sql import func

forms = Blueprint('forms', __name__)

@forms.route('/forms', methods=['GET', 'POST'])
@login_required
def daily_form():
    if request.method == 'POST':
        emotional_state = request.form.get('emotional_state')
        stress_level = request.form.get('stress_level')
        sleep_quality = request.form.get('sleep_quality')
        energy_level = request.form.get('energy_level')
        happiness_level = request.form.get('happiness_level')
        productivity_level = request.form.get('productivity_level')
        water_intake = request.form.get('water_intake')
        physical_exercise = request.form.get('physical_exercise') == 'true'
        meditation = request.form.get('meditation') == 'true'

        today_entry = DailyEntry.query.filter(
            DailyEntry.user_id == current_user.id,
            func.date(DailyEntry.date) == func.date(func.current_timestamp())
        ).first()

        if today_entry:
            flash("You have already completed today's form.", category='error')
            return redirect(url_for('forms.daily_form'))

        if not all([emotional_state, stress_level, sleep_quality, energy_level, happiness_level, productivity_level, water_intake]):
            flash("All fields are required!", category='error')
        else:
            new_entry = DailyEntry(
                emotional_state=emotional_state,
                stress_level=int(stress_level),
                sleep_quality=int(sleep_quality),
                energy_level=int(energy_level),
                happiness_level=float(happiness_level),
                productivity_level=int(productivity_level),
                water_intake=float(water_intake),
                physical_exercise=physical_exercise,
                meditation=meditation,
                user_id=current_user.id
            )
            db.session.add(new_entry)
            db.session.commit()
            flash("Daily entry saved successfully!", category='success')
            return redirect(url_for('home.index'))

    return render_template('forms.html')
