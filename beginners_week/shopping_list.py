shopping_list = []


def show_help():
    print("Available commands:")
    print("- add    <item> : Add an item to the list")
    print("- remove <item> : Remove an item from the list")
    print("- show          : Show the shopping list")
    print("- clear         : Clear the shopping list")
    print("- sort          : Sort the list alphabetically")
    print("- help          : Show this help message")
    print("- quit          : Exit the program")


def add_item(item):
    shopping_list.append(item)
    print(f"{item} added to the list.")


def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the list.")
    else:
        print(f"{item} not found in the list.")


def show_list():
    if shopping_list:
        print("Shopping List:")
        for item in shopping_list:
            print(item)
    else:
        print("The list is empty.")


def clear_list():
    shopping_list.clear()
    print("List cleared.")


def sort_list():
    shopping_list.sort()
    print("List sorted.")


if __name__ == "__main__":
    while True:
        command = input("Enter a command (or 'help' for options): ").lower()

        if command == "add":
            item = input("Enter item to add: ")
            add_item(item)
        elif command == "remove":
            item = input("Enter item to remove: ")
            remove_item(item)
        elif command == "show":
            show_list()
        elif command == "clear":
            clear_list()
        elif command == "sort":
            sort_list()
        elif command == "help":
            show_help()
        elif command == "quit":
            break
        else:
            print("Invalid command. Type 'help' for options.")
