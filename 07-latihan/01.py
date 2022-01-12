max = 5
limit = max
for bintang in range(0, max):
    for pola in range(0, bintang):
        print(" ", end="")
    
    for bentuk in range(0, limit):
        print("*", end="")

    limit -= 1
    print("")