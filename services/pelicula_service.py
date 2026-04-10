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

    # [NUEVO] Método para guardar una película
    @staticmethod
    def crear(titulo, director, puntuacion):
        session = Session()
        try:
            nueva = Pelicula(titulo=titulo, director=director, puntuacion=puntuacion)
            session.add(nueva)
            session.commit()
            print("🚀 DB: Guardado exitoso") # Verás esto en tu terminal
            return True
        except Exception as e:
            print(f"❌ DB ERROR: {e}")
            session.rollback()
            return False
        finally:
            session.close()