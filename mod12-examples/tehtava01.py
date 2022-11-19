# Ulkoisen rajapinnan käyttö:
# Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
# Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/.
# Käyttäjälle on näytettävä pelkkä vitsin teksti.

import requests
from colorama import Fore


def chuck():
    pyynto = "https://api.chucknorris.io/jokes/random"
    try:
        vastaus = requests.get(pyynto)
        if vastaus.status_code == 200:
            vastaus_json = vastaus.json()
            print(vastaus_json["value"])
        elif vastaus == 404:
            print(Fore.RED + "yhteys onnistuu, mutta osoite ei löydy palvelimelta")
        else:
            print(f"{Fore.RED} Yhteys onnistuu, mutta joku virhekoodi: {vastaus.status_code}")

    except requests.exceptions.RequestException as e:
        print(Fore.RED + "Hakua ei voitu suorittaa: " + str(e))


chuck()



