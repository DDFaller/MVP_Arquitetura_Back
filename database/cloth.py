from sqlalchemy import Column, String, Integer, Sequence, LargeBinary,Table
from sqlalchemy.orm import relationship
from base import *

metadata = MetaData(engine,schema='models')
cloth = Table(
    'clothes',metadata,
    Column('id',Integer,Sequence('models.clothes_id_seq',start=1),primary_key=True),
    Column('user_id',Integer),
    Column('model_name',String(140)),
    Column('model_url',String(140))
)

metadata.create_all()