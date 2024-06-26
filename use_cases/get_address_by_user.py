from sqlalchemy.exc import IntegrityError
from logger import logger
from schemas.user_address import apresenta_endereços
from models.user_address import UserAddress
from models.user import User

def get_addresses_by_user(user_id,session):    
    logger.debug(f"Coletando produtos ")
    # fazendo a busca


    addresses = session.query(UserAddress).join(UserAddress.user_id == user_id).all()

    if not addresses:
        # se não há produtos cadastrados
        return {"endereços": []}, 200
    else:
        #logger.debug(f"%d rodutos econtrados" % len(produtos))
        # retorna a representação de produto
        return apresenta_endereços(addresses), 200