#  mengakses dictionary key dengan
x = data_diri['nama'] # bisa juga dengan data_diri.get("nama")
# mengubah value dengan 
data_diri["nama"] = "dian"
# menambahkan entry
data_diri["alamat"] = "jakarta"
# mengapus Key dengan
data_diri.pop("alamat")
# mengecek keberadaan key dengan memakain operator in
if("nama", in data_diri):
    print("nama ada didata diri")