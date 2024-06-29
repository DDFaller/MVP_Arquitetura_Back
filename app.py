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

from apis import *

from use_cases import \
    add_cloth, \
    get_clothes, \
    login_user, \
    register_user, \
    get_cloth


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

@app.post('/login',
           responses={"200": UserLoginSchema,"409": ErrorSchema, "400": ErrorSchema},
           tags=[user_tag])
def login(form: UserSchema):
    session = Session()
    response = login_user(form,session)
    print(response)
    return response

@app.post('/register',
           responses={"200": UserLoginSchema,"409": ErrorSchema, "400": ErrorSchema},
           tags=[user_tag])
def register(form: UserSchema):
    
    session = Session()
    response = register_user(form,session)
    return response




@app.post('/clothes',tags = [cloth_tag],
         responses={'200':ListClothesSchema})
def user_clothes(form: UserIdSchema):
    """Faz a busca por todos os Doutores cadastrados

    Retorna uma representação no formato de uma listagem.
    """
    user_id = form.user_id
    session = Session()
    response = get_clothes(user_id,session)
    for i in range(0,len(response[0]['Roupas'])):
        url = getModelUrl(form.user_id, response[0]['Roupas'][i]['Nome do modelo'])
        response[0]['Roupas'][i]['Bytes do modelo'] = url
    
    session.close()
    return response

@app.post('/cloth', tags=[cloth_tag],
          responses={"200": ClothSchema,"409": ErrorSchema, "400": ErrorSchema})
def post_cloth(form: ClothSchema):
    """Adiciona um novo Agendamento à base de dados

    Retorna os doutores cadastrados na base.
    """
    print(form)
    session = Session()
    response = add_cloth(form,session)
    session.close()
    return response

@app.post('/cloth_model', tags=[cloth_tag],
          responses={"200": ClothSchema,"409": ErrorSchema, "400": ErrorSchema})
def get_cloth_model(form: ClothSchema):
    """Adiciona um novo Agendamento à base de dados

    Retorna os doutores cadastrados na base.
    """
    session = Session()
    response = get_cloth(form,session)
    # Sobrescreve a url do modelo cujo acesso pode já ter expirado por uma nova
    url = getModelUrl(form.user_id, form.model_name)
    response[0]['Bytes do modelo'] = url
    print(response)
    
    session.close()
    return response

