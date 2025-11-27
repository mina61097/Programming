import os

LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def rot13(s):
    out = ""
    for c in s:
        if c in LOWER:
            out += LOWER[(LOWER.index(c) + 13) % 26]
        elif c in UPPER:
            out += UPPER[(UPPER.index(c) + 13) % 26]
        else:
            out += c
    return out


def main():
    print("Travel starting.")

    # Create progress file if missing
    if not os.path.exists("player_progress.txt"):
        with open("player_progress.txt", "w") as f:
            f.write("current_location;next_location;passphrase\n")
            f.write("0;1;qvfpvcyvar\n")

    # Read last progress line
    with open("player_progress.txt") as f:
        last = f.read().strip().split("\n")[-1]

    cur, nxt, cipher_pass = last.split(";")
    cur, nxt = int(cur), int(nxt)
    plain_pass = rot13(cipher_pass)

    print("Currently at home." if cur == 0 else f"Currently at {cur}.")
    print(f"Travelling...\n...Arriving.")
    print("Passing the guard.")
    print(f"\"{plain_pass.capitalize()}!\"")

    # Target ciphered message file
    msg_file = f"{nxt}_{cipher_pass}.gkg"
    print("Looking for the message...")

    with open(msg_file) as f:
        lines = f.read().split("\n")

    print("Found! Seems cryptic.")

    # Save ciphered first line to progress
    with open("player_progress.txt", "a") as f:
        f.write(f"\n{nxt};{nxt+1};{lines[0]}")

    print("[Game] Progress autosaved!")

    # Save deciphered full message
    plain_msg = rot13("\n".join(lines))
    out_file = f"{nxt}-{plain_pass}.txt"
    with open(out_file, "w") as f:
        f.write(plain_msg)

    print("Deciphering Emperor's message...")
    print("Message saved.")
    print("Travel ending.")


if __name__ == "__main__":
    main()
