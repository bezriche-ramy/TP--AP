while True:
    word = input("Please enter a string: ")

    frame_width = 40

    padding = (frame_width - len(word)) // 2

    print("*" * frame_width)
    print("*" + " " * padding + word + " " * padding + "*")
    print("*" * frame_width)