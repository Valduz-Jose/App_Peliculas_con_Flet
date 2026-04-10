from database import Session
from models.pelicula import Pelicula

class PeliculaService:
    @staticmethod
    def obtener_todos():
        session = Session()
        try:
            return session.query(Pelicula).all()
        finally:
            session.close()

    @staticmethod
    def obtener_por_id(id):
        session = Session()
        try:
            return session.query(Pelicula).filter(Pelicula.id == id).first()
        finally:
            session.close()

    @staticmethod
    def crear(titulo, director, puntuacion):
        session = Session()
        try:
            nueva = Pelicula(titulo=titulo, director=director, puntuacion=puntuacion)
            session.add(nueva)
            session.commit()
            print("🚀 DB: Guardado exitoso")
            return True
        except Exception as e:
            print(f"❌ DB ERROR: {e}")
            session.rollback()
            return False
        finally:
            session.close()

    @staticmethod
    def eliminar(id):
        session = Session()
        try:
            peli = session.query(Pelicula).filter(Pelicula.id == id).first()
            if peli:
                session.delete(peli)
                session.commit()
                return True
            return False
        except Exception as e:
            print(f"❌ DB ERROR: {e}")
            session.rollback()
            return False
        finally:
            session.close()

    @staticmethod
    def actualizar(id, titulo, director, puntuacion):
        session = Session()
        try:
            peli = session.query(Pelicula).filter(Pelicula.id == id).first()
            if peli:
                peli.titulo = titulo
                peli.director = director
                peli.puntuacion = puntuacion
                session.commit()
                return True
            return False
        except Exception as e:
            print(f"❌ DB ERROR: {e}")
            session.rollback()
            return False
        finally:
            session.close()