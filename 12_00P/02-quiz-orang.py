from datetime import datetime, date
class Orang:
    linkungan = "RT 2/30 Kelurahan Majujaya"
    def __init__(self, nama, tgl_lahir):
        self.nama_lengkap = nama
        self.tgl_lahir = tgl_lahir

    def tulis_deskiripsi(self):
        today = date.today()
        born = datetime.strptime(self.tgl_lahir, "%d-%m-%Y")
        kalkulasi = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        return f"umur dari {self.nama_lengkap} adalah {kalkulasi}"


def main():
    orang1 = Orang("Budi", "20-03-1987")
    orang2 = Orang("Bayu", "12-05-1988")

    daftar_warga = [orang1, orang2]
    for o in daftar_warga:
        print(o.tulis_deskiripsi())

main()