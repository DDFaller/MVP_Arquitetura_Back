from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.orm import relationship
from  models import Base
from dataclasses import dataclass

@dataclass
class User(Base):
    
    
    __tablename__ = "user_data"
    __table_args__ = {"schema": "user"}

    id = Column(Integer,primary_key=True)
    cpf = Column(String(140))
    password = Column(String(140))