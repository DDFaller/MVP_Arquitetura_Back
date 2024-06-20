from pydantic import BaseModel
from typing import List
from models.user import User 

class UserSchema(BaseModel):
  cpf: str
  password: str

def apresenta_usuario(user):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """

    return {
        "cpf": user.cpf,
        "password": user.password
    }
