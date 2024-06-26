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
    get_clothes \


info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info,template_folder =".")
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
cloth_tag = Tag(name="Roupas", description="Adição, visualização e remoção de agendamentos à base")
user_tag = Tag(name="Usuário", description="Adição, visualização e remoção de doutores da base")
user_address_tag = Tag(name="Endereços", description="Adição, visualização e remoção de clinicas da base")




@app.get('/', tags = [home_tag])
def home():
    """Redireciona para /openapi, tela contendo a documentação.
    """
    return render_template("home.html"), 200

@app.get('/login',
           responses={"200": UserLoginSchema,"409": ErrorSchema, "400": ErrorSchema},
           tags=[user_tag])
def login(form: UserSchema):
    session = Session()
    response = login_user(form,session)
    return response


@app.get('/clothes',tags = [cloth_tag],
         responses={'200':ListClothesSchema})
def all_clothes(form: UserLoginSchema):
    """Faz a busca por todos os Doutores cadastrados

    Retorna uma representação no formato de uma listagem.
    """
    session = Session()
    response = get_clothes(session)
    session.close()
    return response

@app.post('/cloth', tags=[cloth_tag],
          responses={"200": ClothSchema,"409": ErrorSchema, "400": ErrorSchema})
def post_cloth(form: ClothSchema):
    """Adiciona um novo Agendamento à base de dados

    Retorna os doutores cadastrados na base.
    """
    session = Session()
    response = add_cloth(form,session)
    session.close()
    return response


