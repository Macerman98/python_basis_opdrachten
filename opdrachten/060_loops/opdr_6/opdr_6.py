# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

pizzas = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

#sorteren van de pizza's
sorted_pizza = sorted(pizzas)
print(sorted_pizza)
print("\n")

#toevoegen pizza
sorted_pizza.append("zalm")
print(sorted_pizza)
print("\n")

del sorted_pizza[3]
print(sorted_pizza)
print("\n")

#printen eerste drie pizza's
print(sorted_pizza[0:3])

gemiddelde = len(sorted_pizza) // 2
print(gemiddelde)