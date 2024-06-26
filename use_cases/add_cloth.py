from sqlalchemy.exc import IntegrityError
from models.cloth import Cloth
from logger import logger

def add_cloth(form,session):
    """Adiciona um novo Produto à base de dados

    Retorna uma representação dos produtos e comentários associados.
    """
    print(form)
    cloth = Cloth(
        user_id=form.user_id,
        model_name=form.model_name,
        model_bytes=form.model_bytes
        )
    try:
        # adicionando produto
        session.add(cloth)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        return  {"message":"Doutor adicionado"}, 200
    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Produto de mesmo nome e marca já salvo na base :/"
        logger.warning(f"Erro ao adicionar modelo '{cloth.model_name}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar modelo '{cloth.model_name}', {error_msg}")
        return {"mesage": error_msg}, 400