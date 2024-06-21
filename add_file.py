from sqlalchemy import * 
from sqlalchemy.orm import sessionmaker,mapper
import os
from sqlalchemy.sql import text

create_table_models = """
CREATE TABLE IF NOT EXISTS models.clothes
(
	name character varying(40) PRIMARY KEY,
	model_bytes bytea NOT NULL
);
"""


# url de acesso ao banco (essa é uma url de acesso ao sqlite local)
db_url = 'postgresql://postgres:0812@localhost:5432/mvp'

# cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False)
metadata = MetaData(engine)
sample = Table(
    'clothes', metadata,
    Column('id', Integer, primary_key=True),
    Column('model_bytes', LargeBinary),
)
class Sample(object):

    def __init__(self, model_bytes):
        self.model_bytes = model_bytes
mapper(Sample, sample)

metadata.create_all()

# Instancia um criador de seção com o banco
Session = sessionmaker(bind=engine)
session = Session()
# session.execute("CREATE SCHEMA IF NOT EXISTS models")
# session.execute(create_table_models)
# session.commit()

# with open('hamburger.glb','rb') as file:
  
#   obj = Sample(model_bytes=file.read())
#   session.add(obj)
#   session.commit()

modelos = session.query(Sample).all()
print(modelos)

