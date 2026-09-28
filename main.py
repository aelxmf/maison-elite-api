"""
main.py
-------
C'est le point d'entrée de votre API.
Il contient les 4 routes CRUD pour les produits :
  - POST   /produits         -> Créer un produit
  - GET    /produits         -> Lister tous les produits
  - GET    /produits/{id}    -> Lire UN produit précis
  - PUT    /produits/{id}    -> Modifier un produit
  - DELETE /produits/{id}    -> Supprimer un produit

Pour lancer l'API :
  uvicorn main:app --reload

Puis ouvrez dans votre navigateur :
  http://127.0.0.1:8000/docs
  -> une page interactive générée automatiquement pour tester l'API
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select, SQLModel
from typing import List

from database import engine, get_session
from models import Produit, ProduitMiseAJour

app = FastAPI(title="API Maison Élite")

# ==========================================
# CORS : autorise votre site HTML/JS à appeler cette API
# ==========================================
# En développement, "*" autorise toutes les origines (pratique pour tester).
# En production, remplacez "*" par l'adresse exacte de votre site,
# par ex: ["https://www.maison-elite.com"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def au_demarrage():
    """
    Cette fonction s'exécute au démarrage de l'API.
    SQLModel.metadata.create_all crée les tables si elles n'existent pas déjà
    (utile en secours si vous n'avez pas encore exécuté schema.sql).
    """
    SQLModel.metadata.create_all(engine)


# ==========================================
# CREATE - Créer un produit
# ==========================================
@app.post("/produits", response_model=Produit)
def creer_produit(produit: Produit, session: Session = Depends(get_session)):
    session.add(produit)
    session.commit()
    session.refresh(produit)  # récupère l'id généré par MySQL
    return produit


# ==========================================
# READ - Lister tous les produits
# ==========================================
@app.get("/produits", response_model=List[Produit])
def lister_produits(session: Session = Depends(get_session)):
    produits = session.exec(select(Produit)).all()
    return produits


# ==========================================
# READ - Lire un seul produit par son id
# ==========================================
@app.get("/produits/{produit_id}", response_model=Produit)
def lire_produit(produit_id: int, session: Session = Depends(get_session)):
    produit = session.get(Produit, produit_id)
    if not produit:
        raise HTTPException(status_code=404, detail="Produit introuvable")
    return produit


# ==========================================
# UPDATE - Modifier un produit existant
# ==========================================
@app.put("/produits/{produit_id}", response_model=Produit)
def modifier_produit(
    produit_id: int,
    donnees: ProduitMiseAJour,
    session: Session = Depends(get_session),
):
    produit = session.get(Produit, produit_id)
    if not produit:
        raise HTTPException(status_code=404, detail="Produit introuvable")

    # On ne met à jour que les champs réellement envoyés par le client
    donnees_a_modifier = donnees.dict(exclude_unset=True)
    for champ, valeur in donnees_a_modifier.items():
        setattr(produit, champ, valeur)

    session.add(produit)
    session.commit()
    session.refresh(produit)
    return produit


# ==========================================
# DELETE - Supprimer un produit
# ==========================================
@app.delete("/produits/{produit_id}")
def supprimer_produit(produit_id: int, session: Session = Depends(get_session)):
    produit = session.get(Produit, produit_id)
    if not produit:
        raise HTTPException(status_code=404, detail="Produit introuvable")

    session.delete(produit)
    session.commit()
    return {"message": f"Produit {produit_id} supprimé avec succès"}
