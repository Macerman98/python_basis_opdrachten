# Opdracht 2 lists
# Naam student: Mees Post
# Groep:


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

eerste_rivier = rivieren[0].capitalize()
Tweede_land = rivier_info[rivieren[0]][1].capitalize()
print("De rivier " + eerste_rivier + " stroomt onder andere door " + Tweede_land)

tweede_rivier = rivieren[1].capitalize()
eerste_land = rivier_info[rivieren[0]][1].capitalize()
print("De rivier " + tweede_rivier + " stroomt onder andere door " + eerste_land)

derde_rivier = rivieren[2].capitalize()
derde_land = rivier_info[rivieren[2]][0].capitalize()
print("De rivier " + derde_rivier + " stroomt onder andere door " + derde_land)