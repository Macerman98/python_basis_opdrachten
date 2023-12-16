# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier
vragen = [
    "Wat vind je van de huidige regering?",
    "Wat vind je van de Python-lessen tot nu toe?",
    "Wat vind jij de mooiste stad van Nederland?"
]
# vragen
antwoorden = []
for vraag in vragen:
    antwoord = input(f"{vraag}\n")
    antwoorden.append(antwoord)

# Opslaan in bestand
with open("enquete_resultaten.txt", "w") as bestand:
    for i, antwoord in enumerate(antwoorden):
        bestand.write(f"{vragen[i]}\nAntwoord: {antwoord}\n\n")

print("Bedankt voor het invullen van de enquête! De resultaten zijn opgeslagen in enquete_resultaten.txt")
