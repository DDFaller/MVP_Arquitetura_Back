from models.cloth import Cloth
from sqlalchemy.exc import IntegrityError
from logger import logger
from schemas.clothes import apresenta_roupas
from apis import getModelUrl
def get_clothes(user_id,session):
  logger.warning("Realizando busca por modelos")
  roupas = session.query(Cloth).filter(Cloth.user_id == user_id).all()

  if not roupas:
      # se não há produtos cadastrados
      return {"Modelos": []}, 200
  else:
    #Atualiza roupas com base na resposta da API S3
    for roupa in roupas:
        updated_url = getModelUrl(roupa.user_id,roupa.model_name)
        roupa.model_url = updated_url
    
    logger.debug(f"%d Roupas econtradas" % len(roupas))
    # retorna a representação de produto
    return apresenta_roupas(roupas), 200