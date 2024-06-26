from pydantic import BaseModel
from typing import List
from models.user_address import UserAddress 

class UserAddressSchema(BaseModel):
  """ Define como um Endereço a ser inserido deve ser representada
  """
  user_id = int
  cep = str
  city = str
  state = str
  street = str

class ListAddressesSchema(BaseModel):
    """ Define como uma listagem roupas sera retornada
    """
    addresses:List[UserAddressSchema]



def apresenta_endereços(addresses: UserAddress):
  result = []
  for address in addresses:
      result.append(apresenta_endereço(address))

  return {"Endereços":result}


def apresenta_endereço(address):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        'user_id': address.user_id,  
        'cep':address.cep,
        'city':address.city, 
        'state':address.state,
        'street':address.street  
    }
