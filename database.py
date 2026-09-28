"""
database.py
-----------
Ce fichier gère la connexion à ma base de données MySQL.

Les identifiants (utilisateur, mot de passe...)sont lus depuis un fichier .env 
"""

from sqlmodel import create_engine, Session
from sqlalchemy import URL
from dotenv import load_dotenv
import os

# Charge les variables définies dans le fichier .env (s'il existe)
# dans l'environnement du programme, pour qu'on puisse les lire avec os.getenv()
load_dotenv()

UTILISATEUR = os.getenv("DB_UTILISATEUR", "root")
MOT_DE_PASSE = os.getenv("DB_MOT_DE_PASSE", "")
HOTE = os.getenv("DB_HOTE", "localhost")
PORT = int(os.getenv("DB_PORT", "3306"))
NOM_BASE = os.getenv("DB_NOM_BASE", "maison_elite")

# Construction de l'URL de connexion avec URL.create()
# (gère automatiquement les caractères spéciaux dans le mot de passe)
URL_BASE_DE_DONNEES = URL.create(
    drivername="mysql+pymysql",
    username=UTILISATEUR,
    password=MOT_DE_PASSE,
    host=HOTE,
    port=PORT,
    database=NOM_BASE,
)

engine = create_engine(URL_BASE_DE_DONNEES, echo=True)


def get_session():
    """
    Fournit une "session" (une connexion temporaire) à la base de données.
    FastAPI l'utilisera automatiquement pour chaque requête grâce à Depends().
    """
    with Session(engine) as session:
        yield session
