#Este archivo contrendra las consultas a la base de datos
from ORM.modelos import Alumno, Calificacion, Foto
from sqlalchemy.orm import Session
import ORM.esquemas as esquemas

#creamos las funciones que nos serviran como consultas a la base de datos
def obtener_alumnos(sesion:Session):
    # obtenemos todos los alumnos
    return sesion.query(Alumno).all()

def obtener_alumno_id(sesion:Session, id:int):
    # obtenemos el alumno con el id proporcionado
    return sesion.query(Alumno).filter(Alumno.id == id).first()

def insertar_alumno(sesion:Session, alumno:esquemas.AlumnoBase):
    alumno_db = Alumno(nombre=alumno.nombre, edad=alumno.edad, domicilio=alumno.domicilio, email=alumno.email, password=alumno.password)
    sesion.add(alumno_db)
    sesion.commit()
    sesion.refresh(alumno_db)
    print("usuario insertado:", alumno)
    return alumno_db

def actualizar_alumno(sesion:Session, id:int, alumno:esquemas.AlumnoBase):
    alumno_bd = obtener_alumno_id(sesion, id)
    if alumno_bd is not None:
        alumno_bd.nombre = alumno.nombre
        alumno_bd.edad = alumno.edad
        alumno_bd.domicilio = alumno.domicilio
        alumno_bd.email = alumno.email
        alumno_bd.password = alumno.password
        sesion.commit()
        sesion.refresh(alumno_bd)
        print("usuario actualizado:", alumno)
        return alumno
    else:
        return {"mensaje":"usuario no encontrado"}

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

def insertar_calificacion(sesion:Session, id:int, calificacion_esq:esquemas.CalificacionBase):
    calificaion_db = Calificacion(uea = calificacion_esq.uea, calificacion = calificacion_esq.calificacion)
    sesion.add(calificaion_db)
    sesion.commit()
    sesion.refresh(calificaion_db)
    print("usuario insertado:", calificacion_esq)
    return calificaion_db

def actualizar_calificacion(sesion:Session, id:int, calificacion_esq:esquemas.CalificacionBase):
    calificacion_db = obtener_calificacion_id(sesion, id)
    if calificacion_db is not None:
        calificacion_db.uea = calificacion_esq.uea
        calificacion_db.calificacion = calificacion_esq.calificacion
        sesion.commit()
        sesion.refresh(calificacion_db)
        print("calificacion actualizado:", calificacion_esq)
        return calificacion_esq
    else:
        return {"mensaje":"calificacion no encontrado"}
    
def borrar_calificacion_id(sesion:Session, id:int):
    # borramos todas las calificaciones de un alumno
    calificaciones = obtener_calificacion_id(sesion, id)
    if calificaciones is not None:
        for calificacion in calificaciones:
            sesion.delete(calificacion)
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


def borrar_foto_id_alumno(sesion:Session, id_alumno:int):
    # borramos todas las fotos de un alumno
    fotos = obtener_fotos_id_alumno(sesion, id_alumno)
    if fotos is not None:
        for foto in fotos:
            sesion.delete(foto)
        sesion.commit()
    return True

def insertar_foto(sesion:Session, id:int, foto_esq:esquemas.FotoBase):
    foto_db = Foto(titulo = foto_esq.titulo, descripcion = foto_esq.descripcion, ruta = foto_esq.ruta)
    sesion.add(foto_db)
    sesion.commit()
    sesion.refresh(foto_db)
    print("foto insertado:", foto_esq)
    return foto_db

def actualizar_foto(sesion:Session, id:int, foto_esq:esquemas.FotoBase):
    foto_db = obtener_foto_id(sesion, id)
    if foto_db is not None:
        foto_db.titulo = foto_esq.titulo
        foto_db.descripcion = foto_esq.descripcion
        foto_db.ruta = foto_esq.ruta
        sesion.commit()
        sesion.refresh(foto_db)
        print("foto actualizado:", foto_esq)
        return foto_esq
    else:
        return {"mensaje":"foto no encontrado"}