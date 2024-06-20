from logger import logger
from schemas.schedule import apresenta_agendamentos
from models.schedule import Schedule

def get_schedules(session):
    """Faz a busca por todos os agendamentos cadastrados

    Retorna uma listagem dos agendamentos.
    """
    logger.debug(f"Coletando agendamentos ")
    # criando conexão com a base
    # fazendo a busca
    # fazendo a busca
    agendamentos = session.query(Schedule).all()

    if not agendamentos:
        # se não há produtos cadastrados
        return {"agendamentos": []}, 200
    else:
        #logger.debug(f"%d rodutos econtrados" % len(produtos))
        # retorna a representação de produto
        return apresenta_agendamentos(agendamentos), 200