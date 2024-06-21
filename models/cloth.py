from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.orm import relationship
from  models import Base
from dataclasses import dataclass

@dataclass
class Cloth(Base):
    
    
    __tablename__ = "clothes"
    __table_args__ = {"schema": "models"}

    id = Column(Integer,Sequence('models.clothes_id_seq'),primary_key=True)
    user_id = Column(Integer)
    model_name = Column(String(140))
    model_bytes = Column(LargeBinary)