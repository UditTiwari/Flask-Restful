from app import db,app
from sqlalchemy import text

with open("users.sql") as f:
    stm = f.read()
    print(stm)

with app.app_context():
    db.session.execute(text(stm))
    db.session.commit()