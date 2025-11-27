# A8_T1.py
# Menu-driven program template with pause functionality.

import time

def main():
    print("Program starting.")

    pause_duration = 0  # default duration

    while True:
        print("\nOptions:")
        print("1 - Set pause duration")
        print("2 - Activate pause")
        print("0 - Exit")

        choice = input("Your choice: ").strip()

        # Option 1 — Set pause duration
        if choice == "1":
            try:
                pause_duration = float(input("Insert pause duration (s): "))
            except ValueError:
                print("Invalid number. Pause duration unchanged.")

        # Option 2 — Activate pause
        elif choice == "2":
            print(f"Pausing for {pause_duration} seconds.")
            time.sleep(pause_duration)
            print("Unpaused.")

        # Option 0 — Exit
        elif choice == "0":
            print("Exiting program.")
            break

        else:
            print("Invalid choice, try again.")

    print("\nProgram ending.")


if __name__ == "__main__":
    main()
