# Opdracht 2 berekeningen
# Naam student: Mees Post
# Groep:

# Hier komt je code...
gasten = ["Mees", "Paul", "Kees", "Marie", "Hilda"]
print(gasten)

# vraag of er nog mensen thuis blijven:
thuisblijvers = input("Wie blijft er thuis? \n")
if thuisblijvers in gasten:
    gasten.remove(thuisblijvers)
else:
    print(f"{thuisblijvers} staat niet op de gastenlijst")
print("bijgewerkte gastenlijst:")
print(gasten)

# vraag of er nog nieuwe mensen mee gaan:
nieuwe_gast = input("Gaan er nog nieuwe mensen mee? \n")

# nieuwe gast naar Kees:
if nieuwe_gast not in gasten:
    gasten.insert(3, nieuwe_gast)
else:
    print(f"{nieuwe_gast} staat al op de gastenlijst")
print("bijgewerkte gastenlijst:")
print(gasten)