from models.cloth import Cloth
from sqlalchemy.exc import IntegrityError
from logger import logger
from schemas.clothes import apresenta_roupa

def get_cloth(form,session):
  logger.warning("Realizando busca por modelo")

  user_id = form.user_id
  model_name = form.model_name
  roupas = session.query(Cloth).filter(Cloth.user_id == user_id).filter(Cloth.model_name == model_name).first()


  try:
    if not roupas:
      # se não há produtos cadastrados
      return {"Modelos": []}, 200
    else:
        # retorna a representação de produto
        return apresenta_roupa(roupas), 200
  except Exception as e:
    # caso um erro fora do previsto
    error_msg = "Não foi possível obter modelo :/" + str(e)
    logger.warning(f"Erro ao adicionar usuario '{user_id}', {error_msg}")
    return {"mesage": error_msg}, 400