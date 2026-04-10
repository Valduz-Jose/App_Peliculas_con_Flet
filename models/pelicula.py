from sqlalchemy import Column, Integer, String
from database import Base

class Pelicula(Base):
    __tablename__ = "peliculas"

    # Definición de las columnas
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100), nullable=False)
    director = Column(String(100), nullable=False)
    puntuacion = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Pelicula(titulo='{self.titulo}', director='{self.director}', puntuacion={self.puntuacion})>"

# --- CÓDIGO DE PRUEBA ---
if __name__ == "__main__":
    # Creamos un objeto de prueba para verificar que la clase funciona
    peli_test = Pelicula(
        titulo="Batman: El Caballero de la Noche", 
        director="Christopher Nolan", 
        puntuacion=10
    )
    print("✅ Modelo definido correctamente.")
    print(f"Objeto de prueba: {peli_test}")