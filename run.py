from app import create_app

app = create_app()

from app.models import db, User  # Importă modelul User

# Creează baza de date
with app.app_context():
    db.create_all()
    print("Database initialized!")


if __name__ == '__main__':
    app.run(debug=True)
