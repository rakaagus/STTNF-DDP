# Nama Raka Agus Malana
# Nim 0110221186
# TI 18
# 
print("Tugas Fibonacci Rekursi")
print("=======================================")
def fibonacci(nilai):
    if nilai == 0 or nilai == 1:
        return nilai
        
    else:
        return (fibonacci(int(nilai) - 1) + fibonacci(int(nilai) - 2))


parameter = int(input("Masukkan batas deret: "))
n = 1

print("Deret fibonacci: ")
for i in range(1, int(parameter) + 1):
    print(fibonacci(n)," ", end="")
    n += 1