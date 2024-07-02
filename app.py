from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, render_template,request
from urllib.parse import unquote
from sqlalchemy import DateTime
from sqlalchemy import func

from sqlalchemy.exc import IntegrityError
from flask_cors import CORS
from apis import renameFileFromS3

from schemas import *
from models import *
import datetime


from use_cases import \
    add_cloth, \
    get_clothes, \
    login_user, \
    register_user, \
    get_cloth, \
    get_cloth_by_id, \
    delete_cloth


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
    """Retorna login de um Usuário cadastrado na base
    """
    session = Session()
    response = login_user(form,session)
    print(response)
    return response

@app.post('/register',
           responses={"200": UserLoginSchema,"409": ErrorSchema, "400": ErrorSchema},
           tags=[user_tag])
def register(form: UserSchema):
    """Realiza cadastro de um Usuário na base de dados
    """
    session = Session()
    response = register_user(form,session)
    return response

@app.post('/clothes',tags = [cloth_tag],
         responses={'200':ListClothesSchema})
def user_clothes(form: UserIdSchema):
    """Faz a busca por todos os Modelos cadastrados por usuário
    """
    user_id = form.user_id
    session = Session()
    response = get_clothes(user_id,session)
    print('Response received')
    print(response)

    session.close()
    return response

@app.post('/cloth', tags=[cloth_tag],
          responses={"200": ClothSchema,"409": ErrorSchema, "400": ErrorSchema})
def post_cloth(form: ClothSchema):
    """Adiciona um novo Modelo à base de dados
    """
    print(form)
    session = Session()
    response = add_cloth(form,session)
    session.close()
    return response

@app.delete('/cloth', tags=[cloth_tag],
            responses={"200": ClothSchema, "404": ErrorSchema})
def delete_cloth_route(form: RemoveClothSchema):
    """Deleta um Modelo da base de dados

    Retorna a confirmação da deleção.
    """
    session = Session()
    id = form.id
    print(form)
    try:
        cloth = get_cloth_by_id(id, session)
        # Delete the record from the database
        delete_cloth(cloth, session)
        session.commit()
        return {"message": "Deleted successfully"}, 200
    except Exception as e:
        return {"message": str(e)}, 500
    finally:
        session.close()

@app.put('/cloth', tags=[cloth_tag],
         responses={"200": ClothSchema, "404": ErrorSchema, "400": ErrorSchema})
def update_model_name(form: RenameClothSchema):
    """Atualiza o nome do modelo na base de dados
    """
    print(form)
    try:
        session = Session()
        cloth = get_cloth_by_id(form.id, session)
        if not cloth:
            session.close()
            return {"error": "Cloth not found"}, 404
        temp = cloth.model_name
        cloth.model_name = form.model_name
        session.commit()
        renameFileFromS3(cloth.user_id,temp, form.model_name)
        return {'message': f"Object renamed from {temp} to {form.model_name}"}, 200
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
        return {"error": str(e)}, 500
    finally:
        session.close()

@app.post('/cloth_model', tags=[cloth_tag],
          responses={"200": ClothSchema,"409": ErrorSchema, "400": ErrorSchema})
def get_cloth_model(form: ClothSchema):
    """Retorna um modelo cadastrado na base.
    """
    session = Session()
    response = get_cloth(form,session)
    
    session.close()
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)