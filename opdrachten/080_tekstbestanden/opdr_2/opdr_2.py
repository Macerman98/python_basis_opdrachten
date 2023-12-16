# Opdracht 2 
# Naam student: Mees Post
# Groep:



import random

def raad_nummer_spel():
    geheim_getal = random.randint(1, 100)
    aantal_pogingen = 0

    print("Raad mijn geheime getal")

    while True:
        try:
            gebruikers_getal = int(input())
            aantal_pogingen += 1

            if gebruikers_getal < geheim_getal:
                print("hoger")
            elif gebruikers_getal > geheim_getal:
                print("lager")
            else:
                print(f"Je hebt het getal geraden! Het is {geheim_getal}")
                print(f"Je hebt het in {aantal_pogingen} keer geraden")
                break
        except ValueError:
            print("Voer een geldig getal in")

if __name__ == "__main__":
    raad_nummer_spel()