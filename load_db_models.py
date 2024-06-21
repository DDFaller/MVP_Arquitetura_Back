create_schema = """
CREATE SCHEMA IF NOT EXISTS models
"""
create_table_models = """
CREATE TABLE IF NOT EXISTS models.clothes
(
	id serial PRIMARY KEY,
	user_id integer NOT NULL,
    model_name character varying(40) NOT NULL,
	model_bytes character varying(40) NOT NULL
);
"""