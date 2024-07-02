from sqlalchemy.exc import IntegrityError
from models.cloth import Cloth
from logger import logger

def get_cloth_by_id(id,session):
    """Adiciona um novo Produto à base de dados

    Retorna uma representação dos produtos e comentários associados.
    """
    print("GET CLOTH BY ID")
    try:
        cloth = session.query(Cloth).filter(Cloth.id == id).first()
        return cloth
    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Produto de mesmo nome e marca já salvo na base :/"
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/" + str(e)
        logger.warning(f"Erro ao adicionar modelo ")
        return {"mesage": error_msg}, 400