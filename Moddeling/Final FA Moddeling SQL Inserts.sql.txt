-- Insert bonuskaart houders
INSERT INTO bonuskaart (bonuskaartnummer)
VALUES ('65472335');
INSERT INTO bonuskaart (bonuskaartnummer, naam, adress, woonplaats)
VALUES ('12345678','Annette','Vredenburg 12','Utrecht');

-- Insert filiaalen
INSERT INTO filiaal (filiaalnummer, plaats, adres)
VALUES ('35','Utrecht','Stationsplein');
INSERT INTO filiaal (filiaalnummer, plaats, adres)
VALUES ('48','Utrecht','Roelantdreef 41');

-- Insert producten
INSERT INTO product (productnummer, omschrijving, prijs)
VALUES ('1', 'AH halfvolle melk', 0.99);
-- Hier maakte ik een foutje, goeie oefening voor dingen verwijderen
-- INSERT INTO product (productnummer, omschrijving, prijs)
-- VALUES ('2', 'AH halfvolle melk', 2.39);
-- DELETE FROM product
-- WHERE productnummer = 2;
INSERT INTO product (productnummer, omschrijving, prijs)
VALUES ('2', 'AH pindakaas', 2.39);
INSERT INTO product (productnummer, omschrijving, prijs)
VALUES ('3', 'tandelborstel', 1.35);

-- Transactie 1
INSERT INTO transactie (transactienummer, datum, tijd, bonuskaartnummer, filiaalnummer)
VALUES(1, '1/12/2019', '17:35', 65472335, 35);
INSERT INTO aankoop (transactienummer, productnummer, aantal)
VALUES(1, 1, 2);
INSERT INTO aankoop (transactienummer, productnummer, aantal)
VALUES(1, 2, 1);
INSERT INTO aankoop (transactienummer, productnummer, aantal)
VALUES(1, 3, 1);

-- Transactie 2
INSERT INTO transactie (transactienummer, datum, tijd, bonuskaartnummer, filiaalnummer)
VALUES(2, '3/12/2019', '12:25', 65472335, 48);
INSERT INTO aankoop (transactienummer, productnummer, aantal)
VALUES(2,1,1);

-- Transactie 3
INSERT INTO transactie (transactienummer, datum, tijd, bonuskaartnummer, filiaalnummer)
VALUES(3, '1/12/2019', '8:30', 12345678, 35);
INSERT INTO aankoop (transactienummer, productnummer, aantal)
VALUES(3,1,2);

-- Tabellen checken
SELECT * FROM aankoop
SELECT * FROM bonuskaart
SELECT * FROM filiaal
SELECT * FROM product
SELECT * FROM transactie

-- 5 aankopen * aantal gebonden aan transactie nummer
-- dat zijn 7 verkochte producten
-- 2 bonuskaart houders met 1 anonieme
-- 2 filiaalen
-- 3 producten
-- 3 transacties