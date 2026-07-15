import os
from pathlib import Path

from dotenv import load_dotenv

# Ruta del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Cargar variables de entorno
load_dotenv(BASE_DIR / ".env")

# API KEY
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError(
        "No se encontró GOOGLE_API_KEY dentro del archivo .env"
    )

# Directorios
DATA_PATH = BASE_DIR / "data"

VECTOR_DB_PATH = BASE_DIR / "db"