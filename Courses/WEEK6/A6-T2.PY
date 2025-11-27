def main():
    print("Program starting.")

    first = input("Enter first name: ")
    last = input("Enter last name: ")
    filename = input("Enter filename: ")

    # Write file: first name → first line, last name → second line, plus an empty line
    with open(filename, "w") as file:
        file.write(first + "\n")
        file.write(last + "\n")
        file.write("\n") # ensure the file ends with an empty row

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
