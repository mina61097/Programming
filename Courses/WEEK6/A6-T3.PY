def main():
    print("Program starting.")

    first = input("Insert first name: ")
    last = input("Insert last name: ")
    filename = input("Insert filename: ")

    with open(filename, "w") as file:
        file.write(first + "\n")
        file.write(last + "\n")
        file.write("\n") # ensure empty line at end

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
