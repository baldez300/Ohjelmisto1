# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen
# ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina.
# Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen,
# jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key). Selvitä myös,
# miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

import requests
from colorama import Fore

hakusana = input("Anna hakusana: ")


def converter(kelvin):
    return kelvin - 273.15


# '&unites=metric' adding this in the url it will convert degrees to Celsius
pyynto = "https://api.openweathermap.org/data/2.5/weather?q=" + hakusana + "&appid=8db7003ce10ed1c453749b10afb6a750"
try:
    vastaus = requests.get(pyynto)
    if vastaus.status_code == 200:
        vastaus_json = vastaus.json()
        temp = vastaus_json["main"]["temp"]
        celsius = temp-273.15
        print(f"Temperature: {round(celsius)}ºC")

        weather = vastaus_json["weather"][0]["description"]
        print(f"Description: {weather}")

except requests.exceptions.RequestException as e:
    print(Fore.RED + "Hakua ei voitu suorittaa.")