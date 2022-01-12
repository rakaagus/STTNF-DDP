# Nama Raka Agus Malana
# Nim 0110221186
# TI 18
# 
print("Tugas penguraian pemanggilan faktorial rekursi ")
print("=====================================================")
nilai = input("Input nilai: ")
faktor = 1

desc = "faktorial("+nilai+") = 1*"
for i in range(1, int(nilai) + 1):
    if i == int(nilai):
        desc += str(i)+" = "
    
    else:
        desc += str(i)+"*"

    faktor *= i

print(desc+str(faktor))