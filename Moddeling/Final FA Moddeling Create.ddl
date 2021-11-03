CREATE TABLE Aankoop (
  aantal                     int4 NOT NULL, 
  transactienummer int4 NOT NULL, 
  productnummer       int4 NOT NULL);
CREATE TABLE Bonuskaart (
  bonuskaartnummer SERIAL NOT NULL, 
  naam             varchar(255), 
  adress           varchar(255), 
  woonplaats       varchar(255), 
  PRIMARY KEY (bonuskaartnummer));
CREATE TABLE Filiaal (
  filiaalnummer SERIAL NOT NULL, 
  plaats        varchar(255) NOT NULL, 
  adres         varchar(255) NOT NULL, 
  PRIMARY KEY (filiaalnummer));
CREATE TABLE Product (
  productnummer SERIAL NOT NULL, 
  omschrijving  varchar(255) NOT NULL, 
  prijs         numeric(6, 2) NOT NULL, 
  PRIMARY KEY (productnummer));
CREATE TABLE Transactie (
  transactienummer           SERIAL NOT NULL, 
  datum                      date NOT NULL, 
  tijd                       time(7) NOT NULL, 
  bonuskaartnummer int4 NOT NULL, 
  filiaalnummer       int4 NOT NULL, 
  PRIMARY KEY (transactienummer));
ALTER TABLE Aankoop ADD CONSTRAINT FKAankoop554580 FOREIGN KEY (productnummer) REFERENCES Product (productnummer);
ALTER TABLE Aankoop ADD CONSTRAINT FKAankoop426516 FOREIGN KEY (transactienummer) REFERENCES Transactie (transactienummer);
ALTER TABLE Transactie ADD CONSTRAINT FKTransactie507746 FOREIGN KEY (filiaalnummer) REFERENCES Filiaal (filiaalnummer);
ALTER TABLE Transactie ADD CONSTRAINT FKTransactie647021 FOREIGN KEY (bonuskaartnummer) REFERENCES Bonuskaart (bonuskaartnummer);

