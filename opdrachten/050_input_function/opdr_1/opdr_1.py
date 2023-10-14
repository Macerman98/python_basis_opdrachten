# Opdracht 1 input function
# Naam student: Mees Post
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

eerste_vraag = int(input("Geef de lengte van de eerste zijde: \n"))
tweede_vraag = int(input("Geef de lengte van de tweede zijde: \n"))

uitkomst = (eerste_vraag**2 + tweede_vraag**2)
import math
wortel = (math.sqrt(uitkomst))
print(f"De lengte van de schuine zijde is: {wortel:.0f}")
