from generate_password import generate_password


def main():
    # Password Generator
    lowercase = set("abcd")
    uppercase = set("ABCD")
    numbers = set("1234")
    password = generate_password(12, [lowercase, uppercase, numbers])
    print(password)

    # Inventory Management
    inventory = {
        "apple": (10, 50),  # (quantity, price)
        "banana": (5, 75),
        "orange": (3, 125),
    }

    



if __name__ == "__main__":
    main()
