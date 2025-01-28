import statistics

def display_list(user_list, descending=False, reverse=False):
    print("Current List:", user_list)
    if reverse:
        reversed_list = user_list[::-1]
        print("Reversed List:", reversed_list)
    else:
        sorted_list = sorted(user_list, reverse=descending)
        print("Sorted List:", sorted_list)

def calculate_statistics(user_list):
    if user_list:
        mean = statistics.mean(user_list)
        try:
            median = statistics.median(user_list)
            mode = statistics.mode(user_list)
        except statistics.StatisticsError:
            median = None
            mode = None
        print(f"Mean: {mean}")
        print(f"Median: {median}")
        print(f"Mode: {mode}")

def save_to_file(user_list):
    with open("user_list.txt", "a") as file:
        for num in user_list:
            file.write(str(num) + "\n")
    print("List saved to 'user_list.txt'.")

def load_list():
    try:
        with open("user_list.txt", "r") as file:
            loaded_list = [int(line.strip()) for line in file.readlines()]
        return loaded_list
    except FileNotFoundError:
        return []

def clear_list():
    global user_list
    user_list = []
    print("List cleared.")

def remove_number(user_list, number):
    if number in user_list:
        user_list.remove(number)
        print(f"Number {number} removed from the list.")
    else:
        print(f"Number {number} not found in the list.")

# Initialize list
user_list = load_list()

while True:
    try:
        user_input = input("Enter a number (or 'c' to clear, 'r' to remove, 'q' to quit): ")

        if user_input == 'q':
            break
        elif user_input == 'c':
            clear_list()
            continue
        elif user_input == 'r':
            number_to_remove = int(input("Enter the number to remove: "))
            remove_number(user_list, number_to_remove)
            continue

        number = int(user_input)

        if number == 0:
            break

        user_list.append(number)

        display_list(user_list)
        
        calculate_statistics(user_list)

        descending_input = input("Do you want the list sorted in descending order? (y/n): ").lower()
        if descending_input == "y":
            display_list(user_list, descending=True)
        
        reverse_input = input("Do you want to display the list in reverse order? (y/n): ").lower()
        if reverse_input == "y":
            display_list(user_list, reverse=True)
        
        save_input = input("Do you want to save the list to a file? (y/n): ").lower()
        if save_input == "y":
            save_to_file(user_list)
        
    except ValueError:
        print("Please enter a valid number.")
