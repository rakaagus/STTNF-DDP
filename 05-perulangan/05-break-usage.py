daftar_benda=['Meja', 'Kursi', 'Pintu', 'Lemari']
dicari = "Pintu"
panjang_daftar = len(daftar_benda)
for i in range(1, panjang_daftar):
    if daftar_benda[i] == 'Pintu':
        print(f"pintu Ditemukan diposisi {dicari,i}")
        break
    else:
        print(f"{dicari} Tidak Ditemukan")