# Ulkoisen rajapinnan käyttö:
# Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
# Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/.
# Käyttäjälle on näytettävä pelkkä vitsin teksti.

import requests


def chuck():
    pyynto = "https://api.chucknorris.io/jokes/random"
    try:
        vastaus = requests.get(pyynto)
        if vastaus.status_code == 200:
            vastaus_json = vastaus.json()
            print(vastaus_json["value"])

    except requests.exceptions.RequestException as e:
        print("Hakua ei voitu suorittaa.")


chuck()




