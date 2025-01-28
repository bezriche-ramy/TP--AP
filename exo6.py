while (True):
    try:
        price = float(input("Please type in a price: "))

        dinars = int(price)
        centimes=int((price - dinars)*100)

        # Print the results
        print(f"Dinars: {dinars}")
        print(f"Centimes: {centimes}")
        break
    except ValueError:
        print("Please enter a valid Price!")
