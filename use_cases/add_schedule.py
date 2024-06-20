from models.schedule import Schedule
from sqlalchemy.exc import IntegrityError
from logger import logger
from schemas.schedule import apresenta_agendamento

def add_schedule(form,session):
    schedule = Schedule(
        schedule_date = form.schedule_date,
        schedule_time = form.schedule_time,
        clinic_id =     form.clinic_id,
        clinic  =       form.clinic,
        doctor_crm =    form.doctor_crm,

        cpf =           form.cpf,
        patient =       form.patient,
        healthcare =    form.healthcare,
        contact =       form.contact,
        schedule_status = "Ocuppied"
        )
    try:
        # adicionando agendamento
        session.add(schedule)
        session.commit()
        return  {"message":"Agendamento adicionado"}, 200
    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Agendamento já consta na base :/"
        logger.warning(f"Erro ao adicionar agendamento de {schedule.patient} para o dia '{schedule.schedule_date}' '{schedule.schedule_time}', {error_msg}")
        return {"mesage": error_msg}, 409
    
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível adicionar o agendamento :/"
        logger.warning(f"Erro ao adicionar agendamento de {schedule.patient} para o dia '{schedule.schedule_date}' '{schedule.schedule_time}', {error_msg}")
        return apresenta_agendamento(schedule), 400