#Este archivo contrendra las consultas a la base de datos
from ORM.modelos import Alumno, Calificacion, Foto
from ORM.config import SessionClass
from sqlalchemy.orm import Session
from sqlalchemy import and_

#creamos las funciones que nos serviran como consultas a la base de datos
def obtener_alumnos(sesion:Session):
    # obtenemos todos los alumnos
    return sesion.query(Alumno).all()

def obtener_alumno_id(sesion:Session, id:int):
    # obtenemos el alumno con el id proporcionado
    return sesion.query(Alumno).filter(Alumno.id == id).first()

def obtener_fotos(sesion:Session):
    # obtenemos todas las fotos
    return sesion.query(Foto).all()

def obtener_foto_id(sesion:Session, id:int):
    # obtenemos la foto con el id proporcionado
    return sesion.query(Foto).filter(Foto.id == id).first()

def obtener_fotos_id_alumno(sesion:Session, id_alumno:int):
    # obtenemos todas las fotos de un alumno
    return sesion.query(Foto).filter(Foto.id_alumno == id_alumno).all()

def obntener_calificaciones(sesion:Session):
    # obtenemos todas las calificaciones
    return sesion.query(Calificacion).all()

def obtener_calificacion_id(sesion:Session, id:int):
    # obtenemos la calificacion con el id proporcionado
    return sesion.query(Calificacion).filter(Calificacion.id == id).first()

def obtener_calificaciones_id_alumno(sesion:Session, id_alumno:int):
    # obtenemos todas las calificaciones de un alumno
    return sesion.query(Calificacion).filter(Calificacion.id_alumno == id_alumno).all()

def borrar_foto_id_alumno(sesion:Session, id_alumno:int):
    # borramos todas las fotos de un alumno
    fotos = obtener_fotos_id_alumno(sesion, id_alumno)
    if fotos is not None:
        for foto in fotos:
            sesion.delete(foto)
        sesion.commit()
    return True

def borrar_calificacion_id_alumno(sesion:Session, id_alumno:int):
    # borramos todas las calificaciones de un alumno
    calificaciones = obtener_calificaciones_id_alumno(sesion, id_alumno)
    if calificaciones is not None:
        for calificacion in calificaciones:
            sesion.delete(calificacion)
        sesion.commit()
    return True

def borrar_alumno_id(sesion:Session, id:int):
    # borramos el alumno con el id proporcionado
    alumno = obtener_alumno_id(sesion, id)
    if alumno is not None:
        borrar_foto_id_alumno(sesion, id)
        borrar_calificacion_id_alumno(sesion, id)
        sesion.delete(alumno)
        sesion.commit()
    return True

def borrar_fotos_id(sesion:Session, id:int):
    # borramos todas las fotos de un alumno
    fotos = obtener_foto_id(sesion, id)
    if fotos is not None:
        for foto in fotos:
            sesion.delete(foto)
        sesion.commit()
    return True

def borrar_calificacion_id(sesion:Session, id:int):
    # borramos la calificacion con el id proporcionado
    calificacion = obtener_calificacion_id(sesion, id)
    if calificacion is not None:
        sesion.delete(calificacion)
        sesion.commit()
    return True