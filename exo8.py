while(True):
    try:
        number=int(input("Number: "))
        if number // 3 and number // 5:
            print("FizzBuzz")
        elif number // 3 :
            print("Fizz")
        elif number // 5 :
            print("Buzz")
    except ValueError:
        print("Please enter a valid number!")