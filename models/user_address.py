from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.orm import relationship
from  models import Base
from dataclasses import dataclass

@dataclass
class UserAddress(Base):
    
    
    __tablename__ = "user_address"
    __table_args__ = {"schema": "user"}

    id = Column(Integer,Sequence('user.user_address_id_seq'),primary_key=True)
    user_id = Column(Integer)
    cep = Column(String(140))
    city = Column(String(140))
    state = Column(String(140))
    street = Column(String(140))