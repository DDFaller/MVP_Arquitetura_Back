from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# url de acesso ao banco (essa é uma url de acesso ao sqlite local)
db_url = 'postgresql://postgres:0812@db:5432/mvp'

# cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False)

# Instancia um criador de seção com o banco
Session = sessionmaker(bind=engine)
session = Session()

