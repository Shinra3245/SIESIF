import os
from dotenv import load_dotenv

# Encuentra el archivo .env en la raíz del proyecto
basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    """
    Configuración base de la aplicación.
    Lee la URL de la base de datos desde el archivo .env.
    Si no la encuentra, usa un archivo SQLite por defecto.
    """
    
    # Clave secreta para Flask (buena práctica)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una-clave-secreta-muy-dificil'
    
    # Configuración de la Base de Datos
    DATABASE_URL = os.environ.get('DATABASE_URL')
    
    if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

    # Configuración de SQLAlchemy
    SQLALCHEMY_DATABASE_URI = DATABASE_URL or 'sqlite:///' + os.path.join(basedir, 'siesif_app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False