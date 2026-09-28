"""
models.py
---------
Ce fichier décrit la structure d'un "Produit" en Python.
SQLModel se sert de cette classe pour :
  1. Créer/comprendre la table MySQL correspondante
  2. Valider automatiquement les données reçues par l'API
"""

from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class Produit(SQLModel, table=True):
    __tablename__ = "produits"

    id: Optional[int] = Field(default=None, primary_key=True)
    nom: str
    categorie: str
    description: Optional[str] = None
    prix: float
    prix_ancien: Optional[float] = None
    image_url: Optional[str] = None
    badge: Optional[str] = None          # "nouveau", "solde", "bestseller", "limitee"
    taille: Optional[str] = None         # ex: "S, M, L, XL"
    couleur: Optional[str] = None
    stock: int = 0
    date_creation: Optional[datetime] = Field(default_factory=datetime.utcnow)


class ProduitMiseAJour(SQLModel):
    """
    Modèle utilisé uniquement pour la modification (PUT/PATCH) d'un produit.
    Tous les champs sont optionnels : vous pouvez ne modifier qu'un seul champ
    (par exemple juste le prix) sans avoir à renvoyer tout le produit.
    """
    nom: Optional[str] = None
    categorie: Optional[str] = None
    description: Optional[str] = None
    prix: Optional[float] = None
    prix_ancien: Optional[float] = None
    image_url: Optional[str] = None
    badge: Optional[str] = None
    taille: Optional[str] = None
    couleur: Optional[str] = None
    stock: Optional[int] = None
