for i in range(0, 17):
    if i % 2 == 1:
        print(" ", ' '*15, " ")
    elif i > 0 and i < 16:
        if i == 4:
            print("|", " - "*5, "|")
        else : 
            print("|", ' '*15, "|")
    else:
        print("- "*10)