word = input("Please type in a string: ").lower()

vowels = {"a", "e", "i", "o", "u"}
found_vowels = set(word) & vowels  # Intersection entre les lettres du mot et les voyelles

for vowel in sorted(vowels):
    if vowel in found_vowels:
        print(f"{vowel} found!")
    else:
        print(f"{vowel} not found.")