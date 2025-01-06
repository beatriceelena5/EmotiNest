from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, DailyEntry
from flask_login import login_required

forms = Blueprint('forms', __name__)

@forms.route('/forms', methods=['GET', 'POST'])
@login_required
def daily_form():
    if request.method == 'POST':
        emotional_state = request.form.get('emotional_state')
        stress_level = request.form.get('stress_level')
        sleep_quality = request.form.get('sleep_quality')

        # Validează datele
        if not emotional_state or not stress_level or not sleep_quality:
            flash("All fields are required!", category='error')
        else:
            # Salvează în baza de date
            new_entry = DailyEntry(
                emotional_state=emotional_state,
                stress_level=int(stress_level),
                sleep_quality=int(sleep_quality),
                user_id=1  # Temporar, asociere cu un utilizator
            )
            db.session.add(new_entry)
            db.session.commit()
            flash("Daily entry saved successfully!", category='success')
            return redirect(url_for('forms.daily_form'))

    return render_template('forms.html')
