from app import create_app

app = create_app()

from app.models import db, User, Goal, DailyEntry

# Creează sau actualizează baza de date
with app.app_context():
    db.create_all()
    print("Database updated!")


if _name_ == '_main_':
    app.run(debug=True)