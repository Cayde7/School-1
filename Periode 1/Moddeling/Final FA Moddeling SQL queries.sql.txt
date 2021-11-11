-- q1
-- join transactie en filiaal met key filiaalnummer
-- select filiaalnummer, adress, plaats en datum waar bonuskaartnummer
select filiaal.filiaalnummer, adres, plaats, datum from filiaal
left join transactie
on filiaal.filiaalnummer = transactie.filiaalnummer
	where bonuskaartnummer = 65472335

-- q2
-- join aankoop en product met key productnummer waar transactienummer voorkomt
-- select transactie sum aantal * prijs voor totaalprijs waar bonuskaartnummer
select sum(aantal * prijs) as totaalbedrag from aankoop
left join product
on aankoop.productnummer = product.productnummer
where transactienummer in (
	select transactienummer from transactie
	where bonuskaartnummer = 65472335
	);

-- q3
-- join transactie en aankoop met key transactienummer
-- join transactie en filiaal met key filliaalnummer
-- select sum aantal waar filiaal is utrecht en productnummer is 1
select sum(aantal) as aantalverkocht from transactie
left join aankoop
on transactie.transactienummer = aankoop.transactienummer
left join filiaal
on transactie.filiaalnummer = filiaal.filiaalnummer
	where filiaal.plaats = 'Utrecht' and productnummer = 1
