#Este archivo contendra los modelos que mapean las tablas de la base de datos

from ORM.config import BaseClass
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from datetime import datetime

#creamos las clases que representan las tablas de la base de datos
class Alumno(BaseClass):
    __tablename__ = 'alumnos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    edad = Column(Integer)
    domicilio = Column(String(100))
    carrera = Column(String(100))
    trimestre = Column(String(100))
    email = Column('email',String(100))
    password = Column(String(50))
    fecha_registro = Column(DateTime(timezone=True), default=datetime.now)
    
class Calificacion(BaseClass):
    __tablename__ = 'calificaciones'
    id = Column(Integer, primary_key=True)
    id_alumno = Column(Integer, ForeignKey(Alumno.id))
    uea = Column(String(100))
    calificacion = Column(String(100))
    
class Foto(BaseClass):
    __tablename__ = 'fotos'
    id = Column(Integer, primary_key=True)
    id_alumno = Column(Integer, ForeignKey(Alumno.id))
    titulo = Column(String(100))
    descripcion = Column(String(200))
    ruta = Column(String(100))