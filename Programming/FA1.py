uurloon = float(input("Wat is uw uurloon?\n"))
uren = float(input("Hoeveel uur heeft u gewerkt?\n"))
salaris= round(uren*uurloon*100)/100
print(f"{uren} uur levert €{salaris} op.")