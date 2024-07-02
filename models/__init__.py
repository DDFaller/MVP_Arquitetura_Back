from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# importando os elementos definidos no modelo
from models.base import Base
from models.cloth import Cloth
from models.user_address import UserAddress
from models.user import User


# url de acesso ao banco (essa é uma url de acesso ao sqlite local)

database_url = os.getenv('DATABASE_URL')
if not database_url:
    raise ValueError("No DATABASE_URL set for Flask application")

# cria a engine de conexão com o banco
engine = create_engine(database_url, echo=False)

# Instancia um criador de seção com o banco
Session = sessionmaker(bind=engine)
session = Session()


session.commit()

