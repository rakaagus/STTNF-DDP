def tampilkan (nama_mahasiswa, nilai_akhir, nama_matakuliah):
    status=""

    if nilai_akhir > 70:
        status = "Lulus"
    else:
        status = "Mengulang"

    # print("Mahasiswa bernama %s Memiliki nilai %d %s, %s"%(nama_mahasiswa, nama_matakuliah, nilai_akhir, status))
    print(f"Mahasiswa bernama {nama_mahasiswa} meiliki nilai di matkul {nama_matakuliah} {nilai_akhir}, {status}")

tampilkan("Raka Agus Maualan", 80, "DDP")
tampilkan("Dian Aryani", 75, "Bahasa Indonesia")