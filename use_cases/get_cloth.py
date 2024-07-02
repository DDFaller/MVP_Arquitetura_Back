from models.cloth import Cloth
from sqlalchemy.exc import IntegrityError
from logger import logger
from schemas.clothes import apresenta_roupa
from apis import getModelUrl
def get_cloth(form,session):
  logger.warning("Realizando busca por modelo")

  user_id = form.user_id
  model_name = form.model_name
  roupa = session.query(Cloth).filter(Cloth.user_id == user_id).filter(Cloth.model_name == model_name).first()

  try:
    if not roupa:
      # se não há produtos cadastrados
      return {"Modelos": []}, 200
    else:
      # Atualiza url do modelo
      updated_url = getModelUrl(roupa.user_id, roupa.model_name)
      roupa.model_url = updated_url
      # retorna a representação de produto
      return apresenta_roupa(roupa), 200
  except Exception as e:
    # caso um erro fora do previsto
    error_msg = "Não foi possível obter modelo :/" + str(e)
    logger.warning(f"Erro ao adicionar usuario '{user_id}', {error_msg}")
    return {"mesage": error_msg}, 400