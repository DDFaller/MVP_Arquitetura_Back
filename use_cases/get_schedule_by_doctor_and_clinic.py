from logger import logger
from schemas.schedule import apresenta_agendamentos
from models.schedule import Schedule

def get_schedule_by_doctor_clinic(doctor_crm,clinic_id,session):
    
    logger.warning("Coletando agendamentos")
    agendamentos = session.query(Schedule).filter(Schedule.doctor_crm == doctor_crm).filter(Schedule.clinic_id == clinic_id).all()
    
    if not agendamentos:
        # se não há produtos cadastrados
        return {"agendamentos": []}, 200
    else:
        #logger.debug(f"%d rodutos econtrados" % len(produtos))
        # retorna a representação de produto
        print(agendamentos)
        return apresenta_agendamentos(agendamentos), 200