from models.doctor import Doctor
from sqlalchemy.exc import IntegrityError
from logger import logger
from schemas.doctor import apresenta_doutores

def delete_doctor(doctor_crm,session):
    try:
        #logger.debug(f"Coletando produtos ")
        # fazendo a busca
        doctor = session.query(Doctor).filter(Doctor.crm == doctor_crm).delete()
        session.commit()
        if not doctor:
            # se não há produtos cadastrados
            print("Doutor não encontrado")
            return {"mensagem": "Agendamento não encontrado"}, 204
        else:
            logger.debug(f"%d rodutos econtrados" % len(doctor))
            # retorna a representação de produto
            return {"agendamentos": str(doctor)}, 200
        
    except Exception as e:
        error_msg = "Não foi possível excluir o médico :/"
        logger.warning(f"Erro ao remover médico '{doctor_crm}', {error_msg}")
        return {"msg":"Não foi excluir o médico :/"}, 400