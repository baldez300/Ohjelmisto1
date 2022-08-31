
# Ohjelma, joka kysyy nimeni ja sen jälkeen tervehtii minua omalla nimelläni.
name = input("Mikä sinun nimesi on?: ")
print("Terve, " + name + '!')

# sama asia, toinen tapa
print(f"Terve, {name} !")

# kolmas tapa
print("Terve, ", name, '!') # tulee väli kun tulostetaan viimeinen merki.

# neljäs tapa
print("Terve, {}!".format(name))
