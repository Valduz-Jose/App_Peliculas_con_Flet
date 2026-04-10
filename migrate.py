import os
import shutil
from alembic.config import Config
from alembic import command
from database import engine

def run_migrations():
    print("🚀 Iniciando proceso de migración...")
    
    # 1. Configuración de Alembic
    alembic_cfg = Config("alembic.ini")

    try:
        # 2. Intentar generar la revisión automática
        # Esto compara tus clases en Python con las tablas en MySQL
        print("🔍 Detectando cambios en los modelos...")
        command.revision(alembic_cfg, message="Crear tabla peliculas", autogenerate=True)
        
        # 3. Aplicar cambios a la base de datos
        print("🏗️ Aplicando cambios a MySQL...")
        command.upgrade(alembic_cfg, "head")
        
        print("✅ ¡Éxito! La tabla 'peliculas' ha sido creada/actualizada.")
        
    except Exception as e:
        print(f"❌ Error durante la migración: {e}")

if __name__ == "__main__":
    run_migrations()