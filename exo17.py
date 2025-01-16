numbers=[]# 1->5
shoe_size=[]# 8 -> 12
for i in range(5):
    while True:
        number=int(input("enter un nombre entre 1 et 5: "))
        if number in range(6):
            #traitement des doublons 
            if number not in numbers:
                numbers.append(number)
                break
            else:
                print(number,"existe deja dans la liste numbers")
    while True:
        size=int(input("enter un size entre 8 et 12: "))
        if size in range(8,13):
            #traitement des doublons
            if size not in shoe_size:
                shoe_size.append(size)
                break
            else:
                print(size,"existe deja dans la liste shoe_size")
print("Numbers:",numbers)
print("shoe_size:",shoe_size)
print("Numbers + shoe_size:",numbers+shoe_size)
