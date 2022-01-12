# Nama Raka Agus Malana
# Nim 0110221186
# TI 18
#  
nama = "Nurul Fikri"
huruf_vokal = ["a", "i", "u", "e", "o"]

def judul():
    print("menghapus nilai huruf konsonan dari nama nurul fikri")
    print("Menjadi")
    print("==============================================")

def menghapusKonsonanHuruf(nilai):
    for i in nilai:
        if i in huruf_vokal:
            nilai = nilai.replace(i, '')
        nilai = nilai.replace(" ", '')
    print(nilai)


def main():
    judul()
    menghapusKonsonanHuruf(nama)

main()