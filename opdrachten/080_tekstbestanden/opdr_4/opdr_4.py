# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


# Party enquete

def vraag_invoer(vraag_nummer, vraag):
    antwoord = input(f"{vraag_nummer}. {vraag}\n")
    return antwoord

def main():
    vragen = [
        "Wat is je voornaam?",
        "Wat is je achternaam?",
        "Wat neem je mee aan drank?",
        "Wat neem je mee om te eten?"
    ]

    feestgangers = []

    for i, vraag in enumerate(vragen, 1):
        antwoord = vraag_invoer(i, vraag)
        feestgangers.append(antwoord)

    # Maak een dictionary van de antwoorden
    feestganger_dict = {
        "voornaam": feestgangers[0],
        "achternaam": feestgangers[1],
        "drank": feestgangers[2],
        "eten": feestgangers[3]
    }

    # Schrijf de antwoorden naar een tekstbestand
    with open("feestgangers.txt", "a") as bestand:
        bestand.write("----\n")
        for key, value in feestganger_dict.items():
            bestand.write(f"{key}: {value}\n")

    print("\nBedankt voor het invullen!\nSee you at the party.")

if __name__ == "__main__":
    main()
