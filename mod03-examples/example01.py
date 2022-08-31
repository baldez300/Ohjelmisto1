
# Kuhan pituuden laskeminen senttimetreinä.

pituus = float(input("Anna kuhan pituuden (cm): "))
if pituus < 37:
    puuttuva = pituus - 37
    print(f"Laske kuhan takaisin järveen: {puuttuva} (cm) puuttuu!")
elif pituus >= 37:
    print("Nauti kala-ateria!")

