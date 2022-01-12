a = int(input("Masuka Nilai A: "))
b = int(input("Masuka Nilai B: "))
c = int(input("Masuka Nilai C: "))

def determinan(a, b, c):

    determinan = b ** 2 - 4*a*c
    if(determinan == 0):
        print("Memiliki 1 akar tunggal")
    if(determinan > 0):
        print("Punya 2 Akar")
    if(determinan < 0):
        print("tidak memiliki akar")
    print(determinan)

determinan(a,b,c)