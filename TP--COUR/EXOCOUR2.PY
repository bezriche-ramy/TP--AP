import math

while True:
    try:
        number = int(input("Please enter an integer: "))
        if number < 0:
            print("Invalid number")
        elif number > 0:
            print(f"The square root of {number} is {math.sqrt(number)}")
        else:
            break
    except ValueError:
        print("Please enter a valid integer.")