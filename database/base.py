from sqlalchemy import * 
from sqlalchemy.schema import CreateSchema
from sqlalchemy.orm import sessionmaker,mapper
import os
from sqlalchemy.sql import text


database_url = os.getenv('DATABASE_URL')
if not database_url:
    raise ValueError("No DATABASE_URL set for Flask application")


# cria a engine de conexão com o banco
engine = create_engine(database_url, echo=False)
inspector_schemas = inspect(engine).get_schema_names()

with engine.connect() as connection:
    if 'models' not in inspector_schemas:
      connection.execute(CreateSchema("models", if_not_exists=True))
    if 'user' not in inspector_schemas:
      connection.execute(CreateSchema("user", if_not_exists=True))