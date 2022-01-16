baris = 7
kolom = 12
for i in range(0, baris):
    for j in range(baris - 1, i, -1):
        print(".", "", end="")
    for k in range(i):
        print("* "*2, end="")
    for l in range(i + 1, baris):
        print(".", "", end="")
    print()