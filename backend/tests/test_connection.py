from sqlalchemy import text

from app.db.database import engine

try:
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT current_database(), current_user")
        )

        print("Connected Successfully!")
        print(result.fetchone())

except Exception as e:
    print("Connection Failed!")
    print(e)