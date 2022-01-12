# Nama Raka Agus Malana
# Nim 0110221186
# TI 18
# 
print("Tugas Faktorial Rekursi")
print("=======================================")
nilai = input("Masukkan nilai: ")

def faktorial(nilai):
    if nilai == '':
        return None

    parameter = int(nilai)
    if parameter > 2:
        return parameter * faktorial(parameter - 1)

    if parameter == 2:    
        return 2
    
    return 1

nilai_faktor = faktorial(nilai)
print(nilai_faktor)