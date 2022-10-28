# Ulkoisen rajapinnan käyttö:
# Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
# Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/.
# Käyttäjälle on näytettävä pelkkä vitsin teksti.

import requests
import json

url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)
# joke = response.json()["value"]["joke"]
# print(joke)


def chuck():
    f = r"https://api.chucknorris.io/jokes/random/5"
    data = requests.get(f)
    tt = json.loads(data.text)

    print(tt["value"]["joke"])


chuck()