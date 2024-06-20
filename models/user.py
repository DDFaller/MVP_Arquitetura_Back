from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.orm import relationship
from  models import Base
from dataclasses import dataclass

@dataclass
class User(Base):
    
    
    __tablename__ = "user"
    __table_args__ = {"schema": "appointment"}

    cpf = Column(String(140),primary_key=True)
    password = Column(String(140),primary_key=True)