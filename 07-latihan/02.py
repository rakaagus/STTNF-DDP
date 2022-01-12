max = 10
k = 2
for i in range(max, 0, -2):
    for j in range(2, k, 2):
        print(end="  ")
    k += 2
    for j in range(0, i):
        print("*", end=" ")
    print("")