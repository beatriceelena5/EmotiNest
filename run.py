from app import create_app

app = create_app()

from app.models import db, User, Goal  # Importă modelul User

# Creează baza de date
with app.app_context():
    db.create_all()
    print("Database initialized!")


if _name_ == '_main_':
    app.run(debug=True)