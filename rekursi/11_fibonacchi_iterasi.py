# Nama Raka Agus Malana
# Nim 0110221186
# TI 18
# 
print("Tugas Fibonacci Iterasi")
print("=======================================")
nilai = input("Masukkan batas deret: ")
f1 = 1
f2 = 1
next = 0

for i in range(1, int(nilai) + 1):
    if i == 1:
        print(f1, end=" ")
        continue
    
    if i == 2:
        print(f2, end=" ")
        continue

    next = f1 + f2
    f1 = f2
    f2 = next

    print(next, end=" ")