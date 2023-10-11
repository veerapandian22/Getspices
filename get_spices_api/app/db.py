from app.config import settings
import databases
import sqlalchemy
from pydantic import BaseModel


database = databases.Database(settings.connection_string)

metadata = sqlalchemy.MetaData(schema=settings.schema_name)

product_table = sqlalchemy.Table(
    "product",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("product_code", sqlalchemy.String),
    sqlalchemy.Column("product_name", sqlalchemy.String),
    sqlalchemy.Column("product_desc", sqlalchemy.String),
    #sqlalchemy.Column("create_date", sqlalchemy.DateTime),
)


engine = sqlalchemy.create_engine(
    settings.connection_string
)

metadata.create_all(engine)
