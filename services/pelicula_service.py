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