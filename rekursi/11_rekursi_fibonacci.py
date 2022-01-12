# Nama Raka Agus Malana
# Nim 0110221186
# TI 18
# 
print("Tugas penguraian pemanggilan fibonacci rekursi ")
print("=====================================================")
def fibonacci(param):
    if param == 0 or param == 1:
        return param
        
    else:
        return (fibonacci(int(param) - 1) + fibonacci(int(param) - 2))


param = input("Masukkan batas deret: ")
n = 1

print("Deret fibonacci: ", fibonacci(param))

print("\nPenguraian: \n")
f1 = 1
f2 = 1
next = 0

for i in range(1, int(param)):
    if i == 1:
        print(f1, end=" + ")
        continue
    
    if i == 2:
        print(f2, end=" = 1\n")
        continue

    next = f1 + f2
    f1 = f2
    f2 = next

    if i != param:
        print(next, "+",f1," = ",(f2 + f1),end="\n")