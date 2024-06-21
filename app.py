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
    add_cloth, \

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

@app.post('/cloth', tags=[doutor_tag],
          responses={"200": ScheduleSchema,"409": ErrorSchema, "400": ErrorSchema})
def post_doctor(form: ClothSchema):
    """Adiciona um novo Agendamento à base de dados

    Retorna os doutores cadastrados na base.
    """
    session = Session()
    response = add_cloth(form,session)
    session.close()
    return response

@app.delete('/', tags = [doutor_tag])
def remove_doctor(form: RemoveClothSchema):
    """Remove um médico da base

    Retorna 1 caso tenha deletado apenas um médico conforme esperado
    """
    id_to_delete= form.id

    session = session()
    response = delete_cloth(id_to_delete,session)
    session.close()
    return response


