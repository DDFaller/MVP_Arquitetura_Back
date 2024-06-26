from pydantic import BaseModel
from typing import List
from models.user import User 

class UserSchema(BaseModel):
  """ Define com um usuário pode ser definido para criação
  """
  cpf: str
  password: str

class UserLoginSchema(BaseModel):
  """ Define com um usuário pode ser retornado para Login
  """
  id: int
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

def loga_usuario(user):
    return{
        'id':id,
        'cpf': cpf,
        'password':password
    }