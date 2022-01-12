def getAverage(daftar_bilangan):
    count = 0
    sum = 0
    for bilangan in daftar_bilangan:
        count +=1
        sum += bilangan
    if(count == 0):
        return 0 
    return sum/count

daftar = [100, 2, 3, 17, 50]
avg = getAverage(daftar)
print(f"averagi value is {avg}")