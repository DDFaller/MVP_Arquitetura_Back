from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from  models import Base
from dataclasses import dataclass

@dataclass
class DoctorClinic(Base):
    
    
    __tablename__ = "doctor_clinic_mapping"
    __table_args__ = {"schema": "appointment"}


    doctor_crm = Column(String(140),primary_key=True)
    clinic_id = Column(Integer,primary_key=True)
    consults_start = Column(String(140))
    consults_end = Column(String(140))
    estimated_time_per_consult = Column(String(140))
        