def abs(bilangan):
    if bilangan < 0:
        return -bilangan
    return bilangan

for i in range(-5, 7):
    print(abs(i))