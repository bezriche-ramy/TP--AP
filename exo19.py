def count_unique_words():
    unique_words = set()
    total_words = 0
    
    while True:
        word = input("Enter a word: ").strip()
        
        # Handle case-insensitivity
        word_lower = word.lower()
        
        if word_lower in (w.lower() for w in unique_words):
            print(f"You typed in {len(unique_words)} unique words.")
            break
        else:
            unique_words.add(word)
            total_words += 1

# Example usage
count_unique_words()
