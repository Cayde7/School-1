#
# Bevat 2.1-2.3

print("\n[PROG] 2_1. Lists & strings (formatief)")
# We gaan een lijst bijhouden met je favoriete artiesten. We gaan de lijst eerst creëren met 1 artiest en dan uitbreiden. Schrijf per stap een expressie:

"""
1    een nieuwe list met 1 artiest aan te maken met de naam favorieten.
 2   de lijst uit te breiden met een tweede artiest.
  3  de tweede artiest te vervangen door een andere naam.
"""

favorieten = ["Sivu"]
print("Antwoord 1:", favorieten)
favorieten.append("MDK")
print("Antwoord 2:", favorieten)
favorieten[1] = "Zeeslag"
print("Antwoord 3:", favorieten)


print("\n[PROG] 2_2. Lists & numbers")
lst = [3, 7, -2, 12, 36, 19, 2, 5]
print("Antwoord 1: ", max(lst)-min(lst))

print("\n[PROG] 2_3. Tuples")
letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')
lijst =[letters.count("A"), letters.count("B"), letters.count("C")]
print("Antwoord 1: ", lijst)