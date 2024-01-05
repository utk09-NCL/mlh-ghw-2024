import random


def generate_password(length, required_sets):
    characters = set()
    for char_set in required_sets:
        characters.update(char_set)

    password = ""
    while len(password) < length:
        # Convert set to tuple for random.choice
        char = random.choice(tuple(characters))
        password += char
        characters.remove(char)  # Ensure unique characters

        # Enforce combination rules
        if len(password) >= 4 and all(set(password) & char_set for char_set in required_sets):
            break  # Stop if all rules are satisfied

    return password


# Example usage
if __name__ == "__main__":
    # Define character sets
    lowercase = set("abcdefghijklmnopqrstuvwxyz")
    uppercase = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = set("0123456789")
    symbols = set("!@#$%&*_+-?")
    password = generate_password(12, [lowercase, uppercase, numbers, symbols])
    print(password)
