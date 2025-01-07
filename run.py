from app import create_app
from app.models import db, User, Goal, DailyEntry

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database updated!")
    app.run(debug=True, host="0.0.0.0", port=8080)

