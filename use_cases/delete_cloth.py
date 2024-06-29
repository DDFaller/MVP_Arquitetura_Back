from models.cloth import Cloth
from sqlalchemy.exc import IntegrityError
from logger import logger
from schemas.clothes import apresenta_roupas

def delete_cloth(id,session):
    try:
        #logger.debug(f"Coletando produtos ")
        # fazendo a busca
        cloth = session.query(Cloth).filter(Cloth.id == id).delete()
        session.commit()
        if not doctor:
            # se não há produtos cadastrados
            print("Modelo não encontrado")
            return {"mensagem": "Agendamento não encontrado"}, 204
        else:
            logger.debug(f"%d rodutos econtrados" % len(cloth))
            # retorna a representação de produto
            return {"Modelo": str(cloth)}, 200
        
    except Exception as e:
        error_msg = "Não foi possível excluir o médico :/"
        logger.warning(f"Erro ao remover médico '{id}', {error_msg}")
        return {"msg":"Não foi excluir o médico :/"}, 400