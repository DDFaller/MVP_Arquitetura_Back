from models import session
from load_db_sql import *

if __name__ =="__main__":
  #Create tables
  session.execute(create_table_clinics)
  session.execute(create_table_doctor)
  session.execute(create_table_schedules)
  session.execute(create_table_doctor_clinic_mapping)
  #Insert into
  session.execute(insert_into_clinics)
  session.execute(insert_into_doctors)
  session.execute(insert_into_schedules)
  session.execute(insert_into_doctor_clinic_mapping)

  session.commit()
