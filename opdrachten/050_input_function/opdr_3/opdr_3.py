# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...
object_list = input("Noem vijf grote voetballers: \n ")
voetballers = object_list.split(', ')

voetballers.sort(key=lambda x: x.lower(), reverse=True)
print(voetballers)