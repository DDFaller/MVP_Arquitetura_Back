from models.cloth import Cloth
from sqlalchemy.exc import IntegrityError
from logger import logger
from schemas.clothes import apresenta_roupas
from apis import deleteFileFromS3
def delete_cloth(cloth,session):
    try:
        #logger.debug(f"Coletando produtos ")
        # fazendo a busca
        session.delete(cloth)
        session.commit()
        if not cloth:
            # se não há produtos cadastrados
            print("Modelo não encontrado")
            return {"mensagem": "Agendamento não encontrado"}, 204
        else:
            # retorna a representação de produto
            deleteFileFromS3(cloth.user_id, cloth.model_name)
            return {"Modelo": str(cloth)}, 200
        
    except Exception as e:
        raise e
        error_msg = "Não foi possível excluir o modelo :/" + str(e)
        return {"msg":"Não foi excluir o modelo :/"}, 400