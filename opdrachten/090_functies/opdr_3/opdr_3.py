# Opdracht 1 functies
# Naam student:
# Groep: Mees Post

import math

def kubus_vol(zijde):
    volume = zijde**3
    return volume

def bol_vol(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

# voorbeeld vanuit uitleg
zijde_kubus = 100
radius_bol = 50

volume_kubus = kubus_vol(zijde_kubus)
volume_bol = bol_vol(radius_bol)

print(f"De inhoud van deze kubus is: {volume_kubus}")
print(f"De inhoud van deze bol is: {volume_bol}")

