sistema_solar = "Mercurio Venus Tierra Marte Jupiter Saturno Urano Neptuno Pluton"

planetas = set()

for planeta in sistema_solar.split(" "):
    planetas.add(planeta)

print(planetas)
