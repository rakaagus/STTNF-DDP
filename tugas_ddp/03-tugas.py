# Nama Raka Agus Malana
# Nim 0110221186
# TI 18
#  
daftar_buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

def duplikasiDaftarList(nilai):
    array = []
    for i in nilai:
        for j in range(2):
            array.append(i)
    print(array)

def judul():
    print("mengduplikasi nilai dari list")
    print("['pepaya', 'mangga', 'durian', 'jambu']")
    print("Menjadi")
    print("==============================================")   


def main():
    judul()
    duplikasiDaftarList(daftar_buah)

main()
