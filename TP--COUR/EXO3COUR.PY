while True:
    try:
        number = int(input("Please enter a positive integer number: "))
        if number > 0:
            break
        else:
            print("The number must be positive. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer number.")

for i in range(1, number + 1):
    for j in range(1, number + 1):
        print(f"{i} * {j} = {i * j}")
    print()
