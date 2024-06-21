from pydantic import BaseModel
from typing import List
from models.cloth import Cloth 

class ClothSchema(BaseModel):
  """ Define como uma clinica a ser inserida deve ser representada
  """
  id: int = -1
  user_id: int = -1
  model_name: str = 'nome do modelo'
  model_bytes: bytes = b'bytes do modelo'
  

class ListClothesSchema(BaseModel):
    """ Define como uma listagem roupas sera retornada
    """
    clothes:List[ClothSchema]



class RemoveClothSchema(BaseModel):
    """ Define os parâmetros para remoção de uma roupa da base
    """
    id: int = -1


def apresenta_roupas(clothes: Cloth):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for cloth in clothes:
        result.append(apresenta_doutor(doctor))

    return {"roupas":result}



def apresenta_roupa(cloth: Cloth):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "Nome do modelo": cloth.model_name,
        "Bytes do modelo": cloth.model_bytes,
        "ID do usuario": cloth.user_id
    }

