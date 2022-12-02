# Only for training: 1 => (1)(2)

# Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti.
# Jokaisella julkaisulla on nimi.
# Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja.
# Kirjoita luokkiin myös tarvittavat alustajat.
# Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot.
# Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja
# Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

class Publication:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"Julkaisun nimi: {self.name}")


class Magazine(Publication):
    def __init__(self, name, editor):
        self.editor = editor
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f"Olen {self.editor}-päätoimittaja.\n")


class Book(Publication):
    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f"Olen {self.page_count}-sivuinen kirja, kirjailija: {self.author} \n\nKoen vastaukse:\n")


pub1 = Magazine("Aku Ankka", "Aki Hyyppä")
pub2 = Book("Hytti n:o 6", "Rosa Liksom", 200)
pub1.print_info()
pub2.print_info()


# Koen ratkaisu tehtävät
class Suorakulmio:
    def __init__(self, leveys, korkeus):
        self.leveys = leveys
        self.korkeus = korkeus

    def skaalaa (self, kerroin):
        self.leveys = self.leveys * kerroin
        self.korkeus = self.korkeus * kerroin

    def tulosta(self):
        print(f"{self.leveys} x {self.korkeus}")


class Naytto:
    def __init__(self, x_pikselit, y_pikselit):
        self.x_pikselit = x_pikselit
        self.y_pikselit = y_pikselit

    def tulosta(self):
        print(f"Resoluutio: {self.x_pikselit} x {self.y_pikselit}")


class NaytonSuorakulmio(Suorakulmio):
    def __init__(self, leveys, korkeus, x, y, naytto):
        self.x = x
        self.y = y
        self.naytto = naytto
        super().__init__(leveys, korkeus)

    def siirra(self, x_siirtyma, y_siirtyma):
        self.x = self.x + x_siirtyma
        self.y = self.y + y_siirtyma

    def tulosta(self):
        print(f"({self.x} x {self.y})")
        super().tulosta()
        self.naytto.tulosta()


s = Suorakulmio(3, 1)
n = Naytto(1280, 720)
ns = NaytonSuorakulmio(12, 5, 100, 400, n)
n.tulosta()
s.tulosta()
ns.tulosta()
ns.siirra(50, 20)
ns.skaalaa(2)
ns.tulosta()