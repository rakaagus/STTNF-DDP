# Nama Raka Agus Malana
# Nim 0110221186
# TI 18
#  
daftar_buah = ['pepaya', 'mangga', 'durian', 'jambu']

def judul():
    print("Mengreverse nilai dari list berikut")
    print("['pepaya', 'mangga', 'durian', 'jambu']")
    print("Menjadi")
    print("==============================================")


def membalikanNilaiDiList(nilai):
    result = []
    for i in nilai:
        result = [i] + result
    print(result)

def main():
    judul()
    membalikanNilaiDiList(daftar_buah)

main()
