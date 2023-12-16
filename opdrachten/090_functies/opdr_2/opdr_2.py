# Opdracht 1 functies
# Naam student:
# Groep:


def kilometers_naar_miles(kilometers):
    miles = kilometers / 1.609344
    return miles

def miles_naar_kilometers(miles):
    kilometers = miles * 1.609344
    return kilometers

# Voorbeeld van het gebruik van de functies
kilometers = 1223
miles = 867

miles_berekening = kilometers_naar_miles(kilometers)
kilometers_berekening = miles_naar_kilometers(miles)

print(f"{kilometers} kilometers = {miles_berekening} miles")
print(f"{miles} miles = {kilometers_berekening} kilometers")
