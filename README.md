# API Maison Élite

API REST pour gérer les produits de la boutique de mode **Maison Élite** (créer, lister, lire, modifier, supprimer), accompagnée d'un fichier JavaScript pour l'appeler depuis le site.

## Technologies utilisées

- **Python** avec **FastAPI** (framework de l'API)
- **Uvicorn** (serveur)
- **SQLModel** et **PyMySQL** (accès à la base de données)
- **MySQL** (base de données)
- **JavaScript** (appel de l'API depuis le site)

## Contenu du projet

```
maison-elite-api/
├── schema.sql         <- crée la base MySQL et la table produits
├── requirements.txt   <- librairies Python à installer
├── database.py        <- connexion à MySQL (lit les identifiants dans .env)
├── models.py          <- structure d'un produit
├── main.py            <- l'API elle-même (les routes CRUD)
├── .env.example       <- modèle de configuration (sans vraies valeurs)
├── .gitignore         <- fichiers exclus de GitHub (dont .env)
```

## Routes disponibles

| Méthode | Adresse | Rôle |
|---|---|---|
| GET | `/produits` | Lister tous les produits |
| GET | `/produits/{id}` | Lire un produit |
| POST | `/produits` | Créer un produit |
| PUT | `/produits/{id}` | Modifier un produit |
| DELETE | `/produits/{id}` | Supprimer un produit |

La documentation interactive complète est générée automatiquement sur `/docs` une fois l'API lancée.

## Installation

### Étape 1 — Créer la base de données MySQL

1. Assurez-vous que MySQL est installé et lancé sur votre machine.
2. Dans un terminal (ou MySQL Workbench / phpMyAdmin), exécutez :
   ```bash
   mysql -u root -p < schema.sql
   ```
3. Cela crée la base `maison_elite` avec la table `produits`, pré-remplie avec 3 produits d'exemple.

### Étape 2 — Installer les dépendances Python

Dans le dossier du projet :

```bash
pip install -r requirements.txt
```

### Étape 3 — Configurer les identifiants MySQL

Les identifiants sont stockés dans un fichier `.env`, jamais envoyé sur GitHub.

1. Copiez `.env.example` et renommez la copie en `.env`
2. Remplacez les valeurs par vos vrais identifiants :

```
DB_UTILISATEUR=root
DB_MOT_DE_PASSE=votre_mot_de_passe
DB_HOTE=localhost
DB_PORT=3306
DB_NOM_BASE=maison_elite
```

> ⚠️ Le fichier `.env` est listé dans `.gitignore` : il n'est jamais versionné. Seul `.env.example`, qui ne contient aucune information sensible, est publié.

### Étape 4 — Lancer l'API

```bash
uvicorn main:app --reload
```

Le serveur tourne alors sur `http://127.0.0.1:8000`.

## Tester l'API

Ouvrez dans votre navigateur :

```
http://127.0.0.1:8000/docs
```

Cette page interactive (Swagger UI) permet de :
- lister les produits : `GET /produits` → "Try it out" → "Execute"
- créer un produit : `POST /produits` (un formulaire JSON s'affiche)
- modifier (`PUT`) et supprimer (`DELETE`) un produit

## Utiliser l'API depuis le site (JavaScript)

Le fichier `js/api.js`, qui contient les fonctions d'appel à l'API,
se trouve dans le dépôt du site : [maison-elite](https://github.com/TONUSERNAME/maison-elite).

Il est chargé dans `index.html` avec :

<script src="js/api.js"></script>

Fonctions disponibles : `listerProduits`, `lireProduit`, `creerProduit`, `modifierProduit`, `supprimerProduit`. Chacune est documentée avec des exemples en commentaire dans `js/api.js`.

## Erreurs fréquentes

| Message d'erreur | Cause probable |
|---|---|
| `Access denied for user` | Mauvais utilisateur ou mot de passe dans `.env` |
| `Can't connect to MySQL server` | MySQL n'est pas démarré |
| `Unknown database 'maison_elite'` | Le script `schema.sql` n'a pas encore été exécuté |
| Erreur CORS dans la console du navigateur | Vérifiez que l'API tourne bien (`uvicorn main:app --reload`) |

## Améliorations possibles

- Ajouter un formulaire HTML sur le site pour créer, modifier et supprimer des produits sans passer par Swagger
- Ajouter une authentification pour protéger les routes de modification et de suppression
- Héberger l'API en ligne (Render, Railway, PythonAnywhere) et pointer le site vers cette adresse
