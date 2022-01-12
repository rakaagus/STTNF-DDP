# Nama Raka Agus Malana
# Nim 0110221186
# TI 18
#
nilai_akhir = [
{'nama':'Reza', 'nilai':70},
{'nama':'Ciut', 'nilai':63},
{'nama':'Dian', 'nilai':80},
{'nama':'Badu', 'nilai':40}
]

def cari_nama(nama, daftar_nama_siswa):
    hasil = "Nama tidak ditemukan"

    for i in range(len(daftar_nama_siswa)):
        if (daftar_nama_siswa[i].get('nama') == nama):
            hasil = daftar_nama_siswa[i]
        else:
            continue
        
    return hasil

def main():
    print("Tugas Mencari Nama Siswa Yang lulus")
    print("========================================")
    print(cari_nama('Dian', nilai_akhir))

main()


# nilai_akhir = [
# {'nama':'Reza', 'nilai':70},
# {'nama':'Ciut', 'nilai':63},
# {'nama':'Dian', 'nilai':80},
# {'nama':'Badu', 'nilai':40}
# ]

# def cari_nama(nama, daftar_nama_siswa):

#     for i in range(len(daftar_nama_siswa)):
#         if (daftar_nama_siswa[i]['nama'] == nama):
#             print(daftar_nama_siswa[i])
#             continue

# def main():
#     print("Tugas Mencari Nama Siswa Yang lulus")
#     print("========================================")
#     cari_nama('Dian', nilai_akhir)

# main() 