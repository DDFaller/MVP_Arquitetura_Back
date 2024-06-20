from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

from  models import Base
from dataclasses import dataclass

@dataclass
class Schedule(Base):
    
    __tablename__ = "schedules"
    __table_args__ = {"schema": "appointment"}

    schedule_date = Column(DateTime, primary_key=True)
    schedule_time= Column(DateTime,primary_key=True)
    doctor_crm = Column(String(140),ForeignKey("appointment.doctors.crm"))
    clinic_id = Column(Integer,primary_key=True)
    clinic = Column(String(140))
    schedule_status = Column(String(140),nullable=False) #Dois possíveis valores [Available,Ocuppied]
    
    #Dados do paciente
    cpf = Column(String(140))
    patient = Column(String(140))
    contact = Column(String(140))
    healthcare = Column(String(140))