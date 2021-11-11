print("\n[PROG] 3_1. Getallen, Strings and Conversion (formatief) ")

"""
De Hogeschool Utrecht wil studenten financieel ondersteunen bij hun studie, afhankelijk van de cijfers die een student 
haalt. Voor elk cijferpunt krijg je € 30,-. Voor een 1,0 krijg je dus 30 euro, voor een 2,5 krijg je 75 euro en voor 
een 10,0 beloont de HU een student met € 300,-.

Maak variabelen cijferPROJA, cijferPROG en cijferMOD. Geef ze alle drie de waarde die jij verwacht dat je voor de 
betreffende vakken in blok 1 zult gaan halen. Maak nu vervolgens ook de volgende variabelen aan, en bereken de 
bijbehorende waarden m.b.v. een Python expressie:
"""

cijferPROJA = 2
cijferPPROG = 2.5
cijferMOD = 1.5

gemiddelde = ( cijferPROJA + cijferPPROG + cijferMOD ) / 3
beloning = ( cijferPROJA + cijferPPROG + cijferMOD ) * 30

print(f"Mijn cijfers (gemiddeld een {gemiddelde}) leveren een beloning van € {beloning} op!")

print("\n[PROG] 3_2. Operator Precedence ")
# Voeg haakjes toe aan de volgende expressies zodat ze naar True evalueren. Print het resultaat!



print(0 == (1 == 2))
print((2 + (3 == 4) + 5) == 7)
print((1 < -1) == (3 > 4))

print("\n[PROG] 3_3. Input/Output (formatief)")
# Schrijf een programma dat de gebruiker vraagt om zijn uurloon, het aantal uur dat hij of zij gewerkt heeft en dat daarna het salaris uitprint.
"""
Wat verdien je per uur: 3.80
Hoeveel uur heb je gewerkt: 20
20 uur werken levert €76.0 op
"""

uurloon = float(input("Wat is uw uurloon?\n"))
uren = float(input("Hoeveel uur heeft u gewerkt?\n"))
print(f"{uren} uur levert €{round(uren*uurloon*100)/100} op.")
