# En este archivo crearemos la conexión con la base de datos y las sesiones de la API

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#Creamos el enlace a la base de datos
url_base_datos = "postgresql://Joshua_Group:12345@localhost:5432/Practica03"

#Creamos el engine y agregamos los valores para el esquema app
engine = create_engine(url_base_datos, connect_args={"options": "-csearch_path=app"})

#Obtenemos la calse que nos permite crear objetos de sesión
SessionClass = sessionmaker(engine)

#Creamos una función para obtener objetos de la clase session
def generador_session():
    session = SessionClass()
    try:
        yield session
    finally:
        session.close()
        
#Obtenemos la clase base para mapear las tablas
BaseClass = declarative_base()