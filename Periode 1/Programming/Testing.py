def standaardprijs(afstandKM):
    if 0 < afstandKM <= 50:  # afstand is niet kleiner dan 0 en onder 50
        return afstandKM * .8  # return afstand maal 80 cent
    elif afstandKM > 50:  # afstand is meer dan 50
        return 15 + afstandKM * .6  # return vast bedrag plus afstand maal 60 cent
    return 0.0  # afstand is kleiner dan 0 dus return 0 euro, hier had ik eerst een else return maar
    # dat bleek dubbel op te zijn. 0.0 is ingevoerd omdat de output een float moet zijn


def ritprijs(leeftijd, weekendrit, afstandKM):
    stprijs = standaardprijs(afstandKM)  # verminderd function calls, stprijs = standaardprijs

    if weekendrit:  # if True
        if leeftijd < 12 or leeftijd >= 65:
            return stprijs * .65  # weekend, onder 12 of boven/gelijk aan 65 krijgt 35% korting
        else:
            return stprijs * .6  # de rest heeft 40% korting
    else:  # weekend False
        if leeftijd < 12 or leeftijd >= 65:
            return stprijs * .7  # geen weekend, onder 12 of boven/gelijk aan 65 krijgt 30% korting
        else:
            return stprijs  # geen weekend en geen korting leeftijd, betaald standaardprijs
            # is bij de functie standaardprijs() al een float

leeftijd = int(input("Wat is uw leeftijd?\n"))
weekend = bool(input("Reist u in het weekend?\n"))
afstandKM = float(input("Hoeveel KM reist U?\n"))
ritprijs= ritprijs(leeftijd, weekend, afstandKM)
print(f"Uw rit kost €{ritprijs:.2f}")