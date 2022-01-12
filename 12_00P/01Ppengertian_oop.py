class Orang:
    linkungan = "RT 2/30 Kelurahan Majujaya"
    def __init__(self, nama, tgl_lahir):
        self.nama_lengkap = nama
        self.tgl_lahir = tgl_lahir

    def tulis_deskiripsi(self):
        return f"{self.nama_lengkap} lahir pada {self.tgl_lahir}"

orang1 = Orang("Budi", "20-03-1987")
orang2 = Orang("Bayu", "12-05-1988")

print(orang1.tulis_deskiripsi())