from datetime import datetime as dt

class Pegawai:
    honorPerJam = 30000

    def __init__(self, nama, jamKerja):
        self.nama = nama
        self.jamKerja = jamKerja

    def gaji(self):
        gaji = self.jamKerja * Pegawai.honorPerJam
        return f"Gaji Pegawai {self.nama} Sebesar {gaji}"


def main():
    pegawai1 = Pegawai("Udin", 9)

    print(pegawai1.gaji())

main()
