import requests

class filmArsivKaynagi:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_anahtar = "78dfhoiw343uhfuf94uhqewy457"
    def populerleriGetir(self):
        istek = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_anahtar}&languge=tr-TR&page=1")
        return istek.json()
    def filmArat(self, anahtarsozcuk):
        istek = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_anahtar}&query={anahtarsozcuk}page=1")
        return istek.json()

filmApisi = filmArsivKaynagi()

while True:
    secim = input("1- Popüler filmler\n2- Film ara\n3- Çık\nSeçim: ")
    if secim == "3":
        break
    else:
        if secim == "1":
            filmler = filmApisi.populerleriGetir()
            for film in filmler["results"]:
                print(filmler["title"])
        if secim == "2":
            anahtarsozcuk = input("Anahtar sözcük: ")
            filmler = filmApisi.filmArat(anahtarsozcuk)
            for film in filmler["results"]:
                print(filmler["name"])