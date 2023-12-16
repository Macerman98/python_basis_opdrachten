# Opdracht 4 condities
# Naam student: Mees Post
# Groep:



toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00), ("ansjovis", 2.50)]
beschikbare_toppings = [topping[0] for topping in toppings]  # Build the list of available toppings

keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings}\n")

# Kies een topping
found = False
for topping, price in toppings:
    if keuze.lower() == topping.lower():
        print(f"U heeft {topping} besteld. Dat kost {price}")
        found = True
        break

if not found:
    print("Uw keuze zit niet in ons assortiment")
