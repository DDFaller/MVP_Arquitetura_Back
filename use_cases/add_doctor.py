from sqlalchemy.exc import IntegrityError
from models.doctor import Doctor
from logger import logger

def add_doctor(form,session):
    """Adiciona um novo Produto à base de dados

    Retorna uma representação dos produtos e comentários associados.
    """
    print(form)
    doctor = Doctor(
        doctor_name=form.name,
        speciality=form.speciality,
        crm=form.crm
        )
    try:
        # adicionando produto
        session.add(doctor)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        return  {"message":"Doutor adicionado"}, 200
    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Produto de mesmo nome e marca já salvo na base :/"
        logger.warning(f"Erro ao adicionar produto '{doctor.name}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar produto '{doctor.name}', {error_msg}")
        return {"mesage": error_msg}, 400