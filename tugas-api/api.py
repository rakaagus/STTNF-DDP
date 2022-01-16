import requests
from tabulate import tabulate
from os import system


class AnimeCharakter:
        data = []
        total_data = 10
        url = "https://animechan.vercel.app/api/quotes"

        def getAnimeCharacter(self, order = "ASC", page=1):
                header = ['anime', 'Chacter']
                response = requests.get(self.url).json()
                self.data = []
                for i in range(len(response)):
                        self.data.append([i+1, response[i]['anime'], response[i]['character']])
                start = self.total_data * (page - 1)
                self.data = self.data[start:start+self.total_data]
                self.data = sorted(self.data, reverse=True if order == "DESC" else False)
                print(tabulate(self.data, header, tablefmt="Github"))

        def preview(self):
                system('cls')
                print("="*16)
                print("Anime Characters")
                print("="*16)
                print()
                order = input("Urutan Data ASC/DESC : ").upper()
                page = int(input("Halaman : "))
                self.getAnimeCharacter(order, page)
                again = input("Lihat Data Lainnya (Y/N) : ").upper()
                if again == "Y":
                        self.preview()


AnimeCharakter().preview()