for i in range(1,11):
    for j in range(1, 11):
        k = i*j
        print(k, end=" ")
    print()


print()
print("menjadi while")
i = 1
while i <= 11:
    print(i)
    i += 1
    j = 1
    while j <= 11:
        hasil = i*j
        print(hasil, end=" ")
print()