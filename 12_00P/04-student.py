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
        return f"umur dari {self.nama_lengkap} adalah {kalkulasi} tahun"

    def tanggalLahir(self):
        return f"Tanggal Lahir {self.tgl_lahir}"

class Student(Orang):
    def __init__(self, nama, tgl_lahir, tgl_masuk):
        super().__init__(nama, tgl_lahir)
        self.tgl_masuk = tgl_masuk

    def durasi_kuliah(self):
        today = date.today()
        masuk = datetime.strptime(self.tgl_masuk, "%d-%m-%Y")
        kalkulasi = today.year - masuk.year - ((today.month, today.day) < (masuk.month, masuk.day))
        if(kalkulasi == 0):
            return f"{self.nama_lengkap} belum berkuliah selama Setahun, tetapi sudah berkuliah bulan"
        else: 
            return f"Durasi Kuliah {self.nama_lengkap} adalah {kalkulasi} tahun"

def main():
    raka = Student("Raka agus maulana", "22-07-2002", "20-06-2021")

    print(raka.tulis_deskiripsi())
    print("===========================================")
    print(raka.tanggalLahir())
    print("===========================================")
    print(raka.durasi_kuliah())

main()