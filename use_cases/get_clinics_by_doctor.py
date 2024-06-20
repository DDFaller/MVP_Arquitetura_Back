from models.clinic import Clinic
from models.doctor_to_clinic import DoctorClinic
from sqlalchemy.exc import IntegrityError
from logger import logger
from schemas.clinic import show_clinics

def get_clinics_by_doctor(crm,session):    
    logger.debug(f"Coletando produtos ")
    # fazendo a busca


    clinics = session.query(Clinic).join(DoctorClinic,Clinic.id == DoctorClinic.clinic_id).filter(DoctorClinic.doctor_crm == crm).all()

    if not clinics:
        # se não há produtos cadastrados
        return {"consultorios": []}, 200
    else:
        #logger.debug(f"%d rodutos econtrados" % len(produtos))
        # retorna a representação de produto
        return show_clinics(clinics), 200