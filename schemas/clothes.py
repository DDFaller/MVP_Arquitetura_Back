from pydantic import BaseModel
from typing import List
from models.cloth import Cloth 
import base64
import json
class ClothSchema(BaseModel):
  """ Define como um modelo a ser inserido deve ser representada
  """
  user_id: int = -1
  model_name: str = 'nome do modelo'
  model_url: str = 'url do modelo'

class ListClothesSchema(BaseModel):
    """ Define como uma listagem de modelos sera retornada
    """
    clothes:List[ClothSchema]

class RenameClothSchema(BaseModel):
  """ Define como um modelo podera ser renomeado deve ser representada
  """
  id: int = -1
  old_model_name: str = 'nome do modelo'
  model_name: str = 'url do modelo'


class RemoveClothSchema(BaseModel):
    """ Define os parâmetros para remoção de um modelo da base
    """
    id: int = -1



def apresenta_roupas(clothes: Cloth):
    """ Retorna uma representação dos modelos.
    """
    result = []
    for cloth in clothes:
        result.append(apresenta_roupa(cloth))

    return {"Roupas":result}



def apresenta_roupa(cloth: Cloth):
    """ Retorna uma representação do modelo.
    """
    return {
        "ID do modelo": cloth.id,
        "Nome do modelo": cloth.model_name,
        "Bytes do modelo": cloth.model_url,
        "ID do usuario": cloth.user_id
    }

