uurloon = float(input("Wat is uw uurloon?\n"))
uren = float(input("Hoeveel uur heeft u gewerkt?\n"))
print(f"{uren} uur levert €{round(uren*uurloon*100)/100} op.")