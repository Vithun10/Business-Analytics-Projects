from sqlalchemy import inspect
from app.database import engine

inspector = inspect(engine)

print(
    inspector.get_table_names()
)