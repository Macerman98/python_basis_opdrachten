# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

pizzas = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

# Sorteren van de pizza's
sorted_pizza = sorted(pizzas)
print(sorted_pizza)
print("\n")

# Toevoegen pizza
sorted_pizza.append("zalm")
print(sorted_pizza)
print("\n")

# Verwijderen pizza
del sorted_pizza[3]
print(sorted_pizza)
print("\n")

# Printen eerste drie pizza's
print(sorted_pizza[0:3])
print("\n")

# Middelste pizza
gemiddelde = len(sorted_pizza) // 2
print(sorted_pizza[gemiddelde])
print("\n")

# Print de laatste drie pizza's
print(sorted_pizza[-3:])
