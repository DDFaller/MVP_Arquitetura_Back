from models.schedule import Schedule
from logger import logger
from schemas.schedule import apresenta_agendamento

def find_schedule(clinic,date,time,session):
    
    logger.warning(f"Encontrando agendamento Clinica '{clinic}', Date '{date}', Time '{time}'")
    try:
        # fazendo a busca
        schedule = session.query(Schedule).filter(Schedule.schedule_date == date).filter(Schedule.schedule_time == time)\
                   .filter(Schedule.clinic_id == clinic).all()[0]
        if not schedule:
            # se não há produtos cadastrados
            logger.warning("Agendamento não encontrado")
            return {"mensagem": "Agendamento não encontrado"}, 204
        else:
            logger.debug(f"agendamento econtrado")
            # retorna a representação de produto
            return apresenta_agendamento(schedule), 200
        
    except Exception as e:
        print(e)
        error_msg = "item não encontrado :/"
        logger.warning(f"Erro ao procurar agendamento Clinica:'{clinic}' Dia: '{date}' Horario: '{time}', {error_msg}")
        return {"msg":"Não foi possível encontrar o item :/"}, 400