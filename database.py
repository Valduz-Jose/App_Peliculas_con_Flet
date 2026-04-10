import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

# Construir la URL de conexión
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Formato: mysql+pymysql://usuario:password@host:puerto/base
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# engine -> responsable de la conexión física
engine = create_engine(DATABASE_URL)

# Session -> responsable de las operaciones (CRUD)
Session = sessionmaker(bind=engine)

# Base -> Clase de la que heredarán nuestros modelos
Base = declarative_base()

# --- CÓDIGO DE PRUEBA ---
if __name__ == "__main__":
    try:
        with engine.connect() as connection:
            print("✅ ¡Conexión exitosa a MySQL!")
            print(f"Conectado a: {DB_NAME} en {DB_HOST}")
    except Exception as e:
        print(f"❌ Error al conectar: {e}")
        print("Revisa que MySQL esté corriendo y que tus credenciales en .env sean correctas.")