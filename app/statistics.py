from flask import Blueprint, render_template
from .models import db, DailyEntry
from sqlalchemy import func
from datetime import datetime, timedelta

statistics = Blueprint('statistics', __name__)

@statistics.route('/statistics')
def stats():
    # Calculăm datele pentru ultimele 7 zile
    today = datetime.utcnow()
    week_ago = today - timedelta(days=7)

    # Selectăm datele pentru fiecare zi
    weekly_data = db.session.query(
        func.date(DailyEntry.date),
        func.avg(DailyEntry.stress_level),
        func.avg(DailyEntry.sleep_quality)
    ).filter(DailyEntry.date >= week_ago).group_by(func.date(DailyEntry.date)).all()

    # Structurăm datele pentru grafice
    labels = [str(row[0]) for row in weekly_data]
    stress_data = [round(row[1], 2) for row in weekly_data]
    sleep_data = [round(row[2], 2) for row in weekly_data]

    return render_template('statistics.html', labels=labels, stress_data=stress_data, sleep_data=sleep_data)