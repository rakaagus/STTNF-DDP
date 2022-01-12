number = ""
for i in range (1, 10+1):
    if(i == 10):
        i = 0
    number += str(i)
print(""*8, number[0], ""*7, number[1], ""*7, number[2], end="")
print()
print(number*3, end="")