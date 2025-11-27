print("Program starting.")

words = []

while True:
    word = input("Insert word (empty stops): ")
    if word == "":
        print("Close the loop.")
        break
    words.append(word)

total_words = len(words)
total_characters = sum(len(w) for w in words)

print("You inserted:")
print(" -", total_words, "words")
print(" -", total_characters, "characters")
print("Program ending.")
