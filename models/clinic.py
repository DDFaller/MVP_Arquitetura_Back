from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.orm import relationship
from  models import Base
from dataclasses import dataclass

@dataclass
class Clinic(Base):
    
    
    __tablename__ = "clinics"
    __table_args__ = {"schema": "appointment"}

    id = Column(Integer,Sequence('appointment.clinics_id_seq'),primary_key=True)
    name = Column(String(140))
    address = Column(String(140))