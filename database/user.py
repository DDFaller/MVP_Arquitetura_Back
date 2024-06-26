from sqlalchemy import Column, String, Integer, Sequence, LargeBinary,Table
from sqlalchemy.orm import relationship
from base import *


metadata = MetaData(engine,schema='user')
cloth = Table(
    'user_data',metadata,
    Column('id',Integer,Sequence('user.user_id_seq',start=1),primary_key=True),
    Column('cpf',String(140)),
    Column('password',String(140)),
)

metadata.create_all()
