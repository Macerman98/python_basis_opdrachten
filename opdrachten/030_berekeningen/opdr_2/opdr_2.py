# Opdracht 2 berekeningen
# Naam student: Mees Post
# Groep:

# Hier komt je code...
celsius_temp = int(input("Voer de graden in Celsius in: "))
fahrenheit_temp = (celsius_temp*9/5)+32

#print de temperatuur met tekst
print(str(round(celsius_temp)) + " graden Celsius is gelijk aan " + str(round(fahrenheit_temp, 1)) + " graden Fahrenheit")


fahrenheit_temp = int(input("Voer de temperatuur in Fahrenheit in: "))
celsius_temp = (fahrenheit_temp - 32) * 5/9

#print de temperatuur met tekst
print(str(round(fahrenheit_temp, 1)) + " graden Fahrenheit is gelijk aan " + str(round(celsius_temp, 1)) + " graden Celsius")