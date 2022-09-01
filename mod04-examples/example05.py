# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).

valid_username = 'python'
valid_password = 'rules'

tryCount = 0
maxTries = 5

while tryCount < maxTries:
    tryCount += 1
    input_username = input("Käyttäjätunnus?: ")
    input_password = input("Salasana?: ")
    if valid_username == input_username and input_password == valid_password:
        print("Tervetuloa!")
        break
    print("Virhelliset kirjautumistiedot yritä uudelleen..!")
else:
    print("pääsy evätty!")