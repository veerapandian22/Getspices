from app.config import settings
import databases
import sqlalchemy
from pydantic import BaseModel


database = databases.Database(settings.connection_string)

metadata = sqlalchemy.MetaData(schema="SpiceInventory")

notes = sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("text", sqlalchemy.String),
    sqlalchemy.Column("completed", sqlalchemy.Boolean),
)


engine = sqlalchemy.create_engine(
    settings.connection_string, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)
