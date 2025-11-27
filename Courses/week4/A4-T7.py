# Constant for separating words
DELIMITER = ','


def collectWords() -> str:
    """Collects words from user input separated by DELIMITER and returns them as one string."""
    words = []
    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        words.append(word)
    return DELIMITER.join(words)


def analyseWords(PWords: str) -> None:
    """Analyses the given words string and prints word count, total characters, and average word length."""
    if not PWords:
        print("- 0 Words")
        print("- 0 Characters")
        print("- 0.00 Average word length")
        return

    word_list = PWords.split(DELIMITER)
    word_count = len(word_list)
    char_count = sum(len(w) for w in word_list)
    avg_length = char_count / word_count

    print(f"- {word_count} Words")
    print(f"- {char_count} Characters")
    print("- {:.2f} Average word length".format(avg_length))
    return None


def main():
    """Main function to control the program flow."""
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
