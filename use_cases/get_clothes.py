from models.cloth import Cloth
from sqlalchemy.exc import IntegrityError
from logger import logger
from schemas.clothes import apresenta_roupas

def get_clothes(user_id,session):
  logger.warning("Realizando busca por modelos")
  roupas = session.query(Cloth).filter(Cloth.user_id == user_id).all()
  if not roupas:
      # se não há produtos cadastrados
      return {"Modelos": []}, 200
  else:
      logger.debug(f"%d Roupas econtradas" % len(roupas))
      # retorna a representação de produto
      return apresenta_roupas(roupas), 200