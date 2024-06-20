from sqlalchemy.exc import IntegrityError
from models.user import User
from logger import logger
from schemas.user import apresenta_usuario

def login_user(form,session):
    """Adiciona um novo Produto à base de dados

    Retorna uma representação dos produtos e comentários associados.
    """
    print(form)
    user = User(
        cpf=form.cpf,
        password=form.password
        )
    try:
        user_exists = session.query(User).filter(User.cpf == user.cpf).count()
        print(user_exists)
        if user_exists:
          if (session.query(User).filter(User.cpf == user.cpf).filter(User.password == user.password).count()):
            return apresenta_usuario(user), 200
          else:
            return {"message":"Password incorreta"}
        else:
          # adicionando produto
          session.add(user)
          # efetivando o camando de adição de novo item na tabela
          session.commit()
          return  apresenta_usuario(user), 200
    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Usuario já salvo na base :/"
        logger.warning(f"Erro ao adicionar usuario '{user.cpf}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo usuario :/"
        logger.warning(f"Erro ao adicionar usuario '{user.cpf}', {error_msg}")
        return {"mesage": error_msg}, 400