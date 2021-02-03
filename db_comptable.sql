DROP DATABASE IF EXISTS compte;
CREATE DATABASE compte;
USE compte;

-- créer une table clients
DROP TABLE IF EXISTS clients;
CREATE TABLE clients(
    client_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT UNIQUE,
    type_client VARCHAR(50),
    raison_sociale VARCHAR(50),
    email VARCHAR(50),
    adresse VARCHAR(50),
    tel VARCHAR(50)
);

-- créer une table factures
DROP TABLE IF EXISTS factures;
CREATE TABLE factures(
    num_facture INT PRIMARY KEY NOT NULL AUTO_INCREMENT UNIQUE,
    date_emission DATE,
    total INT,
	Fk_client_id INT,
	FOREIGN KEY (Fk_client_id) REFERENCES clients(client_id) ON DELETE SET NULL ON UPDATE CASCADE
);

-- créer une table produits
DROP TABLE IF EXISTS produits;
CREATE TABLE produits(
    produit_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT UNIQUE,
    nom_produit VARCHAR(50),
    ref_produit VARCHAR(50),
    prix_unite INT
);

-- créer une table de liens entre factures et produits
DROP TABLE IF EXISTS liens_produits_factures;
CREATE TABLE liens_produits_factures (
    Fk_facture_id INT,
    Fk_produit_id INT,
    quantite INT,
    FOREIGN KEY (Fk_facture_id) REFERENCES factures(num_facture) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (Fk_produit_id) REFERENCES produits(produit_id) ON DELETE CASCADE ON UPDATE CASCADE
);