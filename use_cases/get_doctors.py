from models.doctor import Doctor
from sqlalchemy.exc import IntegrityError
from logger import logger
from schemas.doctor import apresenta_doutores

def get_doctors(session):
  logger.warning("Realizando busca por doutores")
  doutores = session.query(Doctor).all()

  if not doutores:
      # se não há produtos cadastrados
      return {"doutores": []}, 200
  else:
      logger.debug(f"%d rodutos econtrados" % len(doutores))
      # retorna a representação de produto
      return apresenta_doutores(doutores), 200