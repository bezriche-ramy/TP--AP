while(True):
    try:
        Temperature=int(input("Please enter the temperature in Celsius : "))
        if Temperature<0:
            print("It's freezing!")

        if Temperature<10:
            print("It's cold!")

        if Temperature<20:
            print("It's cool!")    

        print("Stay safe!")
        break
    except ValueError:
        print("Please enter a valid number!")
