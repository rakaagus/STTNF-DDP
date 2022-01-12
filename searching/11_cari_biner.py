# Nama Raka Agus Malana
# Nim 0110221186
# TI 18
#  
biner_linear = [1, 2, 4, 5, 10, 12, 20, 21, 23, 25, 30, 34, 50, 67, 99, 100, 102, 110]

def cari_biner(array, x):
    l = 0
    u = len(array) - 1

    while l <= u:
        mid = l + (u - l)//2
        if array[mid] == x:
            return True
        elif array[mid] < x:
            l = mid + 1
        else:
            u = mid - 1
    return False

def main():
    print("Tugas Mencari nilai biner")
    print("==========================================================")
    hasil = cari_biner(biner_linear, 5)

    if hasil:
        print("Ketemu")
    else:
        print("Tidak ada")

main()