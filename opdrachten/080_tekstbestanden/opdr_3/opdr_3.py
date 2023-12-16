# Opdracht 3 Tekst opslaan
# Naam student: Mees Post
# Groep:


#Hier komt je code
def encrypteer(tekst):
    versleutelde_tekst = ""
    for karakter in tekst:
        if karakter.isalpha():
            # Encrypteer alleen letters
            verschuiving = 5
            basis = ord('A') if karakter.isupper() else ord('a')
            versleuteld_karakter = chr((ord(karakter) - basis + verschuiving) % 26 + basis)
            versleutelde_tekst += versleuteld_karakter
        else:
            # Behoud niet-alfabetische tekens
            versleutelde_tekst += karakter
    return versleutelde_tekst

def decrypteer(versleutelde_tekst):
    ontsleutelde_tekst = ""
    for karakter in versleutelde_tekst:
        if karakter.isalpha():
            # Decrypteer alleen letters
            verschuiving = 5
            basis = ord('A') if karakter.isupper() else ord('a')
            ontsleuteld_karakter = chr((ord(karakter) - basis - verschuiving) % 26 + basis)
            ontsleutelde_tekst += ontsleuteld_karakter
        else:
            # Behoud niet-alfabetische tekens
            ontsleutelde_tekst += karakter
    return ontsleutelde_tekst

if __name__ == "__main__":
    # Vraag om invoer
    tekst = input("Geef de tekst die je wilt encrypten of decrypten:\n")

    # Encrypteer de tekst
    versleutelde_tekst = encrypteer(tekst)
    print(f"Versleutelde tekst: {versleutelde_tekst}")

    # Decrypteer de versleutelde tekst
    ontsleutelde_tekst = decrypteer(versleutelde_tekst)
    print(f"Ontsleutelde tekst: {ontsleutelde_tekst}")
