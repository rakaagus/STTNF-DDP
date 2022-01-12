# Nama Raka Agus Malana
# Nim 0110221186
# TI 18
#  

hasil_akhir = [
    {'nama': 'Reza', 'nilai': 70},
    {'nama': 'Ciut', 'nilai': 63},
    {'nama': 'Dian', 'nilai': 80},
    {'nama': 'Badu', 'nilai': 40}
]

def judul():
    print("Mencari Nilai siswa yang lulus")
    print("==============================================")

def mencariSiswaYangLulus(nilai):
    nama = []
    for i in range(len(nilai)):
        if nilai[i]['nilai'] > 65:
            nama.append(nilai[i]['nama'])
    return nama


def main():
    judul()
    hasil = mencariSiswaYangLulus(hasil_akhir)
    print(hasil)

main()