from pydantic import BaseModel
from typing import List
from models.doctor import Doctor 

class DoctorSchema(BaseModel):
  """ Define como um doutor é apresentado na base de dados
  """
  name: str = "Dr. Frederico"
  speciality: str = "Cardiologista"
  crm: str = "0000"

class FindDoctorSchema(BaseModel):
  """ Define como um doutor deve ser buscado na base de dados
  """
  crm: str = "0000"

class ListDoctorSchema(BaseModel):
    """ Define uma listagem de doutores
    """
    doctors:List[DoctorSchema]

class RemoveDoctorSchema(BaseModel):
    """ Define os parâmetros para remoção de um doutor da base
    """
    crm: str = "0000"

def apresenta_doutores(doctors: Doctor):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for doctor in doctors:
        result.append(apresenta_doutor(doctor))

    return {"doutores":result}



def apresenta_doutor(doctor: Doctor):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "Doutor": doctor.name,
        "Especialidade": doctor.speciality,
        "CRM": doctor.crm
    }

