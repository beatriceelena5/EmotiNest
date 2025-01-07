from flask import Blueprint, render_template
from .models import db, DailyEntry
from sqlalchemy import func
from datetime import datetime, timedelta

statistics = Blueprint('statistics', __name__)

@statistics.route('/statistics')
def stats():
    today = datetime.utcnow()
    week_ago = today - timedelta(days=7)

    weekly_data = db.session.query(
        func.date(DailyEntry.date),
        func.avg(DailyEntry.stress_level),
        func.avg(DailyEntry.sleep_quality),
        func.avg(DailyEntry.energy_level),
        func.avg(DailyEntry.productivity_level),
        func.avg(DailyEntry.water_intake),
        func.sum(DailyEntry.physical_exercise),
        func.sum(DailyEntry.meditation)
    ).filter(DailyEntry.date >= week_ago).group_by(func.date(DailyEntry.date)).all()

    labels = [str(row[0]) for row in weekly_data]
    stress_data = [round(row[1], 2) for row in weekly_data]
    sleep_data = [round(row[2], 2) for row in weekly_data]
    energy_data = [round(row[3], 2) for row in weekly_data]
    productivity_data = [round(row[4], 2) for row in weekly_data]
    water_data = [round(row[5], 2) for row in weekly_data]
    physical_exercise_data = [int(row[6]) for row in weekly_data]
    meditation_data = [int(row[7]) for row in weekly_data]

    return render_template(
        'statistics.html',
        labels=labels,
        stress_data=stress_data,
        sleep_data=sleep_data,
        energy_data=energy_data,
        productivity_data=productivity_data,
        water_data=water_data,
        physical_exercise_data=physical_exercise_data,
        meditation_data=meditation_data
    )
