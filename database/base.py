from sqlalchemy import * 
from sqlalchemy.schema import CreateSchema
from sqlalchemy.orm import sessionmaker,mapper
import os
from sqlalchemy.sql import text


db_url = 'postgresql://postgres:0812@localhost:5432/mvp'

# cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False)
inspector_schemas = inspect(engine).get_schema_names()

with engine.connect() as connection:
    if 'models' not in inspector_schemas:
      connection.execute(CreateSchema("models", if_not_exists=True))
    if 'user' not in inspector_schemas:
      connection.execute(CreateSchema("user", if_not_exists=True))