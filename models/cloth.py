from sqlalchemy import Column, String, Integer, Sequence, LargeBinary
from sqlalchemy.orm import relationship
from  models import Base
from dataclasses import dataclass



@dataclass
class Cloth(Base):
    
    
    __tablename__ = "clothes"
    __table_args__ = {"schema": "models"}

    id = Column(Integer,primary_key=True)
    user_id = Column(Integer)
    model_name = Column(String(140))
    model_url = Column(String(140))