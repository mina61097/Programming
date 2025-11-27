"""Prints the given word inside a decorative frame."""
    frame_length = len(PWord) + 4 # 2 spaces + 2 stars
    print('*' * frame_length)
    print(f"* {PWord} *")
    print('*' * frame_length)
    return None


def main():
    """Main function of the program."""
    print("Program starting.")
    print() # Empty line
    word = input("Insert word: ")
    frameWord(word)
    print()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
