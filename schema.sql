-- =========================================
-- Script de création de la base de données
-- Maison Élite
-- =========================================
-- Comment utiliser ce fichier :
-- 1. Ouvrez MySQL Workbench, phpMyAdmin, ou votre terminal MySQL
-- 2. Copiez-collez tout ce fichier et exécutez-le
--    (ou en ligne de commande : mysql -u root -p < schema.sql)

-- Crée la base de données si elle n'existe pas déjà
CREATE DATABASE IF NOT EXISTS maison_elite
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

-- On se place dans cette base de données
USE maison_elite;

-- Crée la table "produits"
CREATE TABLE IF NOT EXISTS produits (
    id             INT AUTO_INCREMENT PRIMARY KEY,
    nom            VARCHAR(255)   NOT NULL,
    categorie      VARCHAR(100)   NOT NULL,
    description    TEXT           NULL,
    prix           DECIMAL(10,2)  NOT NULL,
    prix_ancien    DECIMAL(10,2)  NULL,
    image_url      VARCHAR(500)   NULL,
    badge          VARCHAR(50)    NULL,
    taille         VARCHAR(100)   NULL,
    couleur        VARCHAR(100)   NULL,
    stock          INT            NOT NULL DEFAULT 0,
    date_creation  TIMESTAMP      DEFAULT CURRENT_TIMESTAMP
);

-- (Optionnel) Quelques produits d'exemple pour tester tout de suite
-- Vous pouvez supprimer ce bloc si vous préférez partir d'une table vide
INSERT INTO produits (nom, categorie, description, prix, prix_ancien, image_url, badge, taille, couleur, stock)
VALUES
('Manteau en laine mérinos', 'MANTEAUX', 'Un manteau chaud et élégant en laine mérinos, coupe intemporelle.', 890.00, NULL, 'image/Piece_1_nouv.jpg', 'nouveau', 'S, M, L, XL', 'Beige', 12),
('Robe mi-longue structurée', 'ROBES', 'Robe blanche structurée, parfaite pour toute occasion.', 520.00, 780.00, 'image/Piece_1_solde.jpg', 'solde', 'XS, S, M', 'Blanc', 5),
('Blazer à double boutonnage', 'VESTES', 'Blazer classique à double boutonnage.', 640.00, NULL, 'image/Piece_1_blaz.jpg', NULL, 'S, M, L', 'Noir', 8);
