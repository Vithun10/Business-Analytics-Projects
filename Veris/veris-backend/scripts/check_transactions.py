from app.database import SessionLocal

from app.models.db_models import (
    Transaction
)

db = SessionLocal()

count = (
    db.query(Transaction)
    .count()
)

print(
    f"Transactions: {count}"
)

db.close()