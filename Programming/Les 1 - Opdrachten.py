#
# Bevat 1.1-1.4

print("\n[PROG] 1_1. Expressions")
# Noteer van elke expressie wat de uitkomst en het type is!

print("Expressie | Uitkomst  | Type\n5         | 5         | Int\n5.0       | 5.0       | Float\n5 % 2     | 1         | Int\n5 > 1     | True      | Bool\n'5'       | '5'       | Str\n5 * 2     | 10        | Int")

print("\n[PROG] 1_2. Strings")
# Schrijf en evalueer Python expressies die de volgende vragen beantwoorden:

"""
1     Hoeveel letters zijn er in 'Supercalifragilisticexpialidocious'?
 2    Komt in 'Supercalifragilisticexpialidocious' de tekst 'ice' voor?
  3   Is het woord 'Antidisestablishmentarianism' langer dan 'Honorificabilitudinitatibus'?
   4  Welke componist komt in alfabetische volgorde het eerst: 'Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'?
    5 Welke het laatst in het rijtje van vraag 4?
"""

print("Antwoord 1:", len("Supercalifragilisticexpialidocious"))
print("Antwoord 2:", "Supercalifragilisticexpialidocious" in "ice")
print("Antwoord 3:", len("Antidisestablishmentarianism") > len("Honorificabilitudinitatibus"))
componisten = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
componisten.sort()
print("Antwoord 4: " + componisten[0])
print("Antwoord 5: " + componisten[-1])

print("\n[PROG] 1_3. Statements")
# schrijf Python statements die het volgende doen

"""
Ken de waarde 6 toe aan variabele a, en waarde 7 aan variabele b.
Ken aan variabele c als waarde het gemiddelde van a en b
Ken aan variabelen voornaam, tussenvoegsel en achternaam je eigen naamgegevens toe.
Ken aan variabele mijnnaam de variabelen van opdracht 3 (met spaties er tussen) toe.
"""
a = 6
b = 7
print("Antwoord 1: var a: ", a, " Var b: ", b)
c = (a+b)/2
print("Antwoord 2: ", c)
voornaam = "Jasper"
tussenvoegsel = "van den"
achternaam = "Bremer"
print("Antwoord 3: ", voornaam, tussenvoegsel, achternaam)
mijnNaam = voornaam + " " + tussenvoegsel + " " + achternaam
print("Antwoord 4: ", mijnNaam)

print("\n[PROG] 1_4. Boolean Expressions (formatief)")
#Schrijf booleaanse expressies die van de variabelen evalueren
print("Antwoord 1:", 6.75 > a < b)
print("Antwoord 2:", len(mijnNaam) == len(voornaam+tussenvoegsel+achternaam))
print("Antwoord 3:", len(str(5*c)) <= len(mijnNaam))
print("Antwoord 4:", tussenvoegsel in achternaam)
