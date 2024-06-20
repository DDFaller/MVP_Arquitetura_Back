from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# importando os elementos definidos no modelo
from models.base import Base
from models.schedule import Schedule
from models.doctor_to_clinic import DoctorClinic
from models.doctor import Doctor
from models.clinic import Clinic



# url de acesso ao banco (essa é uma url de acesso ao sqlite local)
db_url = 'postgresql://postgres:0812@localhost:5432/mvp'

# cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False)

# Instancia um criador de seção com o banco
Session = sessionmaker(bind=engine)
session = Session()

session.execute("CREATE SCHEMA IF NOT EXISTS appointment")
session.commit()

