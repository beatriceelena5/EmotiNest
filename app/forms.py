from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, DailyEntry
from flask_login import login_required, current_user

forms = Blueprint('forms', __name__)

@forms.route('/forms', methods=['GET', 'POST'])
@login_required
def daily_form():
    if request.method == 'POST':
        emotional_state = request.form.get('emotional_state')
        stress_level = request.form.get('stress_level')
        sleep_quality = request.form.get('sleep_quality')
        energy_level = request.form.get('energy_level')
        productivity_level = request.form.get('productivity_level')
        water_intake = request.form.get('water_intake')
        physical_exercise = bool(request.form.get('physical_exercise'))
        meditation = bool(request.form.get('meditation'))

        # Validează datele
        if not (emotional_state and stress_level and sleep_quality and energy_level and productivity_level and water_intake):
            flash("All fields are required!", category='error')
        else:
            # Salvează în baza de date
            new_entry = DailyEntry(
                emotional_state=emotional_state,
                stress_level=int(stress_level),
                sleep_quality=int(sleep_quality),
                energy_level=int(energy_level),
                productivity_level=int(productivity_level),
                water_intake=float(water_intake),
                physical_exercise=physical_exercise,
                meditation=meditation,
                user_id=current_user.id
            )
            db.session.add(new_entry)
            db.session.commit()
            flash("Daily entry saved successfully!", category='success')
            return redirect(url_for('forms.daily_form'))

    return render_template('forms.html')
