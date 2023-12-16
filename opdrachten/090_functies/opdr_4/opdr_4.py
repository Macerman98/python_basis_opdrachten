# Opdracht 1 functies
# Naam student:
# Groep: Mees Post

def volledige_naam(lijst_met_namen):
    for persoon in lijst_met_namen:
        # Bouw de volledige naam op
        volledige_naam = persoon["voornaam"]
        if persoon["tussenvoegsel"]:
            volledige_naam += f" {persoon['tussenvoegsel']}"
        volledige_naam += f" {persoon['achternaam']}"

        # Verwijder dubbele spaties
        volledige_naam = ' '.join(volledige_naam.split())

        # Print de volledige naam
        print(volledige_naam)

# Gegeven lijst met namen
namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

# Roep de functie aan met de gegeven lijst met namen
volledige_naam(namen)
