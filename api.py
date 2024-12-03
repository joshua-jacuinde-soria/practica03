#Este archivo contiene las funciones de ruta para la pagina web

from fastapi import FastAPI, Depends
from ORM import repo
from ORM.config import generador_session
from sqlalchemy.orm import Session

# creación del servidor
app = FastAPI()

#Bienvenida 
@app.get("/")
def hola_mundo():
    print("invocando a ruta /")
    respuesta = {
        "mensaje": "hola mundo!"
    }

    return respuesta

#Creación de funciones de ruta
@app.get("/alumnos")
def obtener_alumnos(sesion: Session = Depends(generador_session)):
    return repo.obtener_alumnos(sesion)

@app.get("/alumnos/{id}")
def obtener_alumno_por_id(id: int, sesion: Session = Depends(generador_session)):
    return repo.obtener_alumno_id(sesion, id)

@app.get("/alumnos/{id}/calificaciones")
def obtener_calificaciones_alumno(id: int, sesion: Session = Depends(generador_session)):
    return repo.obtener_calificaciones_id_alumno(sesion, id)

@app.get("/alumnos/{id}/fotos")
def obtener_foto_alumno(id: int, sesion: Session = Depends(generador_session)):
    return repo.obtener_fotos_id_alumno(sesion, id)

@app.get("/fotos")
def obtener_fotos(sesion: Session = Depends(generador_session)):
    return repo.obtener_fotos(sesion)

@app.get("/fotos/{id}")
def obtener_fotos_id(id: int, sesion: Session = Depends(generador_session)):
    return repo.obtener_foto_id(sesion, id)

@app.get("/calificaciones")
def obtener_calificaciones(sesion: Session = Depends(generador_session)):
    return repo.obntener_calificaciones(sesion)

@app.get("/calificaciones/{id}")
def obtener_calificaciones_id(id: int, sesion: Session = Depends(generador_session)):
    return repo.obtener_calificacion_id(sesion, id)

@app.delete("/foto/{id}")
def borrar_foto_id(id: int, sesion: Session = Depends(generador_session)):
    repo.borrar_fotos_id(sesion, id)
    return {"mensaje": "Foto borrada"}

@app.delete("/calificacion/{id}")
def borrar_calificacion_id(id: int, sesion: Session = Depends(generador_session)):
    repo.borrar_calificacion_id(sesion, id)
    return {"mensaje": "Calificación borrada"}

@app.delete("/alumno/{id}/calificaciones")
def borrar_calificaciones_id_alumno(id: int, sesion: Session = Depends(generador_session)):
    repo.borrar_calificacion_id_alumno(sesion, id)
    return {"mensaje": "Calificaciones de alumno borradas"}

@app.delete("/alumno/{id}/fotos")
def borrar_fotos_id_alumno(id: int, sesion: Session = Depends(generador_session)):
    repo.borrar_foto_id_alumno(sesion, id)
    return {"mensaje": "Fotos de alumno borradas"}

@app.delete("/alumno/{id}")
def borrar_alumno_id(id: int, sesion: Session = Depends(generador_session)):
    repo.borrar_alumno_id(sesion, id)
    return {"mensaje": "Alumno borrado"}
