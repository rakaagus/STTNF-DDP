# Nama Raka Agus Malana
# Nim 0110221186
# TI 18
# 
print("Tugas faktorial Iterasi")
print("=======================================")
nilai = input("Input nilai: ")
faktor = 1

for i in range(1, int(nilai) + 1):
  faktor *= i

print(faktor)