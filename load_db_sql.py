create_schema = """
CREATE SCHEMA IF NOT EXISTS appointment
"""
create_table_doctor = """
CREATE TABLE IF NOT EXISTS appointment.doctors
(
	crm character varying(40) PRIMARY KEY,
	name character varying(40) NOT NULL,
	speciality character varying(40)
);
"""

create_table_clinics="""
CREATE TABLE IF NOT EXISTS appointment.clinics
(
	id serial PRIMARY KEY,
	name character varying(40),
	address character varying(40)
);
"""
create_table_schedules="""
CREATE TABLE IF NOT EXISTS appointment.schedules
(
	doctor_crm character varying(40),
	schedule_date date NOT NULL,
  schedule_time time(0) without time zone NOT NULL,
	clinic_id integer,
  clinic character varying(40) COLLATE pg_catalog."default" NOT NULL,
	schedule_status character varying(40) COLLATE pg_catalog."default" NOT NULL,
	
  cpf character varying(40),
  contact character varying(40) COLLATE pg_catalog."default",
	patient character varying(40) COLLATE pg_catalog."default",
  healthcare character varying(40) COLLATE pg_catalog."default",
  CONSTRAINT schedules_pkey PRIMARY KEY (schedule_date, schedule_time,clinic_id,doctor_crm),
	CONSTRAINT doctor_fkey FOREIGN KEY (doctor_crm) REFERENCES appointment.doctors(crm) ON DELETE CASCADE,
	CONSTRAINT clinic_fkey FOREIGN KEY (clinic_id) REFERENCES appointment.clinics(id) ON DELETE CASCADE

);
"""

create_table_doctor_clinic_mapping = """
CREATE TABLE IF NOT EXISTS appointment.doctor_clinic_mapping
(
	clinic_id integer,
	doctor_crm character varying(40),
	consults_start time(1),
	consults_end time(1),
	estimated_time_per_consult time(4),
	CONSTRAINT doctor_to_clinic PRIMARY KEY (clinic_id, doctor_crm),
	CONSTRAINT doctor_fkey FOREIGN KEY (doctor_crm) REFERENCES appointment.doctors(crm) ON DELETE CASCADE,
	CONSTRAINT clinic_fkey FOREIGN KEY (clinic_id) REFERENCES appointment.clinics(id) ON DELETE CASCADE
);
"""

insert_into_doctors = """
INSERT INTO appointment.doctors(crm,name,speciality) VALUES ('3711','Pete Ross','Cardiologista');
INSERT INTO appointment.doctors(crm,name,speciality) VALUES ('3804','Chloe Sullivan','Ortopedista');
INSERT INTO appointment.doctors(crm,name,speciality) VALUES ('3845','Lana Lang','Ortopedista');
INSERT INTO appointment.doctors(crm,name,speciality) VALUES ('3900','Whitney Fordman','Otorrinolaringologista');
"""

insert_into_clinics="""
INSERT INTO appointment.clinics (id,name,address) VALUES 
(DEFAULT,'Clinica Lang','Rua Visconde de Pirajá');
INSERT INTO appointment.clinics (id,name,address) VALUES 
(DEFAULT,'Clinica Ross','Rua Barao da torre');
INSERT INTO appointment.clinics (id,name,address) VALUES 
(DEFAULT,'Clinica Fordman','Rua Prudente');
"""

insert_into_schedules="""
INSERT INTO appointment.schedules (doctor_crm,schedule_date,schedule_time,schedule_status,clinic,clinic_id,cpf,contact,patient,healthcare)
VALUES ('3845', '26/09/2023','10:00:00','Ocuppied','Clinica Lang',1,'14258613790','21989038580','Daniel','Unimed');

INSERT INTO appointment.schedules (doctor_crm,schedule_date,schedule_time,schedule_status,clinic,clinic_id,cpf,contact,patient,healthcare)
VALUES ('3804', '25/09/2023','11:00:00','Ocuppied','Clinica Lang',1 ,'14258613790','21989038580','Daniel','Unimed');

INSERT INTO appointment.schedules (doctor_crm,schedule_date,schedule_time,schedule_status,clinic,clinic_id,cpf,contact,patient,healthcare)
VALUES ('3711', '25/09/2023','11:00:00','Ocuppied','Clinica Ross',2,'14258613790','21989038580','Daniel','Unimed');
INSERT INTO appointment.schedules (doctor_crm,schedule_date,schedule_time,schedule_status,clinic,clinic_id,cpf,contact,patient,healthcare)
VALUES ('3900', '26/09/2023','11:00:00','Ocuppied','Clinica Fordman',3,'14258613790','21989038580','Daniel','Unimed');
"""

insert_into_doctor_clinic_mapping="""
insert into appointment.doctor_clinic_mapping (clinic_id,doctor_crm, consults_start,consults_end, estimated_time_per_consult)
VALUES (1,'3845','09:00:00','14:00:00','00:15:00');
insert into appointment.doctor_clinic_mapping (clinic_id,doctor_crm, consults_start,consults_end, estimated_time_per_consult)
VALUES (1,'3804','11:00:00','18:00:00','00:15:00');
insert into appointment.doctor_clinic_mapping (clinic_id,doctor_crm, consults_start,consults_end, estimated_time_per_consult)
VALUES (2,'3711','08:00:00','19:00:00','00:45:00');
insert into appointment.doctor_clinic_mapping (clinic_id,doctor_crm, consults_start,consults_end, estimated_time_per_consult)
VALUES (3,'3900','08:00:00','20:00:00','00:30:00');
"""