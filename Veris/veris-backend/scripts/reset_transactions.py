from sqlalchemy import text

from app.database import SessionLocal

db = SessionLocal()

try:
    db.execute(text("DELETE FROM audit_logs"))
    db.execute(text("DELETE FROM transactions"))

    db.commit()

    print("Database reset completed successfully")

except Exception as e:
    db.rollback()
    print("Error:", e)

finally:
    db.close()