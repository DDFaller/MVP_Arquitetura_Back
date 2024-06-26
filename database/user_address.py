from sqlalchemy import Column, String, Integer, Sequence, LargeBinary,Table
from sqlalchemy.orm import relationship
from base import *

metadata = MetaData(engine,schema='user')
cloth = Table(
    'user_address',metadata,
    Column('id',Integer,Sequence('user.user_address_id_seq',start=1),primary_key=True),
    Column('user_id',Integer),
    Column('cep',String(140)),
    Column('city',String(140)),
    Column('state',String(140)),
    Column('street',String(140))
)

metadata.create_all()
