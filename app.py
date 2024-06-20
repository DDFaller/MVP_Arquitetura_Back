from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, render_template,request
from urllib.parse import unquote
from sqlalchemy import DateTime
from sqlalchemy import func

from sqlalchemy.exc import IntegrityError


from flask_cors import CORS

from schemas import *
from models import *
import datetime

from use_cases import \
    add_doctor, \
    add_schedule,\
    get_schedule_by_doctor_clinic,\
    get_schedules, \
    get_doctors,\
    get_clinics,\
    get_clinics_by_doctor,\
    delete_schedules,\
    delete_doctor,\
    login_user,\
    find_schedule

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info,template_folder =".")
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
agendamento_tag = Tag(name="Agendamento", description="Adição, visualização e remoção de agendamentos à base")
doutor_tag = Tag(name="Médico", description="Adição, visualização e remoção de doutores da base")
clinica_tag = Tag(name="Clinica", description="Adição, visualização e remoção de clinicas da base")




@app.get('/', tags = [home_tag])
def home():
    """Redireciona para /openapi, tela contendo a documentação.
    """
    return render_template("home.html"), 200


@app.post('/login', methods =['GET','POST'],
           responses={"200": ScheduleSchema,"409": ErrorSchema, "400": ErrorSchema})
def login(form: UserSchema):
    session = Session()
    response = login_user(form,session)
    return response


@app.post('/agendamento', tags=[agendamento_tag],
          responses={"200": ScheduleSchema,"409": ErrorSchema, "400": ErrorSchema})
def post_schedule(form: ScheduleSchema):
    """Adiciona um novo Agendamento à base

    Retorna uma representação dos agendamentos.
    """
    session = Session()
    response = add_schedule(form,session)
    session.close()
    return response

@app.post('/encontrar_agendamentos', tags=[agendamento_tag],
         responses={"200": ListagemSchedulesSchema})
def schedule_by_doctor_and_clinic(form: SchedulePerDoctorClinicSchema):
    """Faz a busca por todos os agendamentos cadastrados

    Retorna uma listagem dos agendamentos.
    """
    doctor_crm = form.doctor_crm
    clinic = form.clinic_id
    session = Session()
    response = get_schedule_by_doctor_clinic(doctor_crm,clinic,session)
    session.close()
    return response

@app.post('/encontrar_agendamento', tags=[agendamento_tag],
         responses={"200": ScheduleSchema})
def find_a_schedule(form: FindScheduleSchema):
    """Faz a busca por todos os agendamentos cadastrados

    Retorna uma listagem dos agendamentos.
    """

    clinic = form.clinic
    schedule_date = form.schedule_date
    schedule_time = form.schedule_time
    schedule_date = datetime.datetime.strptime(schedule_date,'%d/%m/%Y').strftime('%Y-%m-%d')
    schedule_time = schedule_time + ":00"
    session = Session()
    response = find_schedule(clinic,schedule_date,schedule_time,session)
    session.close()
    return response

@app.get('/agendamentos', tags=[agendamento_tag],
         responses={"200": ListagemSchedulesSchema})
def schedules():
    """Faz a busca por todos os agendamentos cadastrados

    Retorna uma representação da listagem dos agendamentos.
    """
    session = Session()
    response = get_schedules(session)
    session.close()
    return response


@app.delete('/agendamento',tags = [agendamento_tag],
            responses={"200":ListClinicSchema})
def remove_a_schedule(form: DeleteScheduleSchema):
    """Deleta um agendamento da base

     Retorna 1 caso tenha deletado apenas um agendamento conforme esperado
    """
    clinic_to_delete = form.clinic_id
    date_to_delete = form.schedule_date
    time_to_delete = form.schedule_time
    cpf_to_delete = form.cpf


    date_to_delete = datetime.datetime.strptime(date_to_delete,'%d/%m/%Y').strftime('%Y-%m-%d')
    time_to_delete = time_to_delete + ":00"
    session = Session()
    response = delete_schedules(clinic_to_delete,date_to_delete,time_to_delete,cpf_to_delete,session)
    session.close()
    return response

@app.get('/doutores',tags = [doutor_tag],
         responses={'200':ListDoctorSchema})
def all_doctors():
    """Faz a busca por todos os Doutores cadastrados

    Retorna uma representação no formato de uma listagem.
    """
    session = Session()
    response = get_doctors(session)
    session.close()
    return response

@app.post('/doutor', tags=[doutor_tag],
          responses={"200": ScheduleSchema,"409": ErrorSchema, "400": ErrorSchema})
def post_doctor(form: DoctorSchema):
    """Adiciona um novo Agendamento à base de dados

    Retorna os doutores cadastrados na base.
    """
    session = Session()
    response = add_doctor(form,session)
    session.close()
    return response

@app.delete('/doutor', tags = [doutor_tag])
def remove_doctor(form: RemoveDoctorSchema):
    """Remove um médico da base

    Retorna 1 caso tenha deletado apenas um médico conforme esperado
    """
    doctor_crm = form.crm

    session = session()
    response = delete_doctor(doctor_crm,session)
    session.close()
    return response



@app.post('/encontrar_consultorio',tags = [clinica_tag],
         responses={'200':ScheduleSchema})
def clinics_of_doctor(form: FindDoctorSchema):
    """Faz a busca por todos os consultórios onde um médico faz atendimento

    Retorna uma representação no formato de uma listagem.
    """
    doctor_crm = form.crm

    session = Session()
    response = get_clinics_by_doctor(doctor_crm,session)

    session.close()
    return response

@app.get('/consultorios',tags = [clinica_tag],
         responses={'200':ListClinicSchema})
def clinics():
    """Faz a busca por todos os consultórios 

    Retorna uma representação no formato de uma listagem.
    """
    session = Session()
    response = get_clinics(session)
    session.close()
    return response
