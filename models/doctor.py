from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from  models import Base
from dataclasses import dataclass

@dataclass
class Doctor(Base):
    
    __tablename__ = "doctors"
    __table_args__ = {"schema": "appointment"}

    crm = Column(String(140),primary_key=True)
    name = Column(String(140))
    speciality = Column(String(140))
        
