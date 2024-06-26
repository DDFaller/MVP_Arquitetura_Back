from models.cloth import Cloth
from sqlalchemy.exc import IntegrityError
from logger import logger
from schemas.clothes import apresenta_roupas

def get_clothes(session):
  logger.warning("Realizando busca por doutores")
  roupas = session.query(Cloth).all()

  if not roupas:
      # se não há produtos cadastrados
      return {"roupas": []}, 200
  else:
      logger.debug(f"%d rodutos econtrados" % len(roupas))
      # retorna a representação de produto
      return apresenta_roupas(roupas), 200