# Nama Raka Agus Malana
# Nim 0110221186
# TI 18
#
data = [10, 20, 15, 75, 90, 65, 100]

def cari_max(array):
    max = 0
    position = 0

    for i in range(len(array)):
        if array[i] == 90:
            max = array[i]
            position = i

        else:

            continue
            
    return position

def main():
    print("Tugas Mencari nilai Terbesar")
    print("==========================================================")
    print("Posisi dengan nilai terbesar:", cari_max(data))

main()