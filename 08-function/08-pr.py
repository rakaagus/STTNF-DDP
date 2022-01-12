# Nama Raka Agus Malana
# Nim 0110221186
# TI 18
#  
import math
def judul():
    print("Selamat Datang Di Kalkulator Persamaan Kuadrat")
    print("ABC")
    print("==============================================")

def mencariAkar(a, b, c, determinan):

    # masukan rumus
    if(determinan == 0):
        x1 = (-b-math.sqrt(determinan))/(2*a)
        x2 = (-b+math.sqrt(determinan))/(2*a)
        x1 = x2
        print(f"Karena Determinan = 0, maka x1 = {x1} dan x2 = {x2}")
    elif(determinan > 0):
        x1 = (-b-math.sqrt(determinan))/(2*a)
        x2 = (-b+math.sqrt(determinan))/(2*a)
        print(f"Nilai Determinan > 0, Maka :")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif(determinan < 0):
        print("Akar Imajiner, tidak memiliki akar nyata")

def mencariDeterminan(a,b,c):
    
    # rumus determinan
    determinan = b**2 - 4*a*c
    
    if(determinan == 0):
        print("Punya Akar 1 tunggal")
    elif(determinan > 0):
        print("Punya 2 Akar")
    elif(determinan < 0):
        print("Tidak Punya Akar Nyata")
    print(f"Nilai Determinanya Adalah: {determinan}")

    mencariAkar(a, b, c, determinan)
    

def subKalkulator():
    print("Silahkan Masukan Nilai A, B, C Terlebih Dahulu")

def main():
    judul()
    subKalkulator()
    a = int(input("Masukan Nilai A: "))
    b = int(input("Masukan Nilai B: "))
    c = int(input("Masukan Nilai C: "))
    if(a == 0):
        print("Maaf Nilai A Tidak Boleh Kosong!!")
        question = str(input("Silahkan Ulang program Dengan (Yes[Y]/No[N]): "))
        if(question == "Y"):
            main()
        else:
            print("Terima Kasih")
    else:
        mencariDeterminan(a, b, c)
        print("Terima Kasih")
        question_2 = str(input("Mau Mencoba Lagi?(Yes[Y] / No[N]): "))
        if(question_2 == "Y"):
            main()
        else:
            print("Terima Kasih Telah Mencoba prgram ini")

main()