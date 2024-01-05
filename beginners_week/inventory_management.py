inventory = {
    "apple": (10, 1.50),  # (quantity, price)
    "banana": (5, 0.75),
    "orange": (3, 1.25),
}


def display_inventory():
    print("\nInventory:")
    for item, (quantity, price) in inventory.items():
        total_cost = quantity * price
        print(
            f">> {item}: {quantity} units at ${price:.2f} each (${total_cost:.2f} total)")


def sell_item(item, quantity):
    print(f"\n## Attempting to sell {quantity} {item}(s)...")
    if item in inventory and quantity <= inventory[item][0]:
        inventory[item] = (inventory[item][0] - quantity, inventory[item][1])
        print(f"\n## -- Sold {quantity} {item}(s).")
    else:
        print(
            f"\n## Cannot sell {quantity} {item}(s). Insufficient stock or item not found.")


def add_item(item, quantity, price):
    if item in inventory:
        inventory[item] = (
            inventory[item][0] + quantity, (inventory[item][1] + price) / 2)
    else:
        inventory[item] = (quantity, price)
    print(f"\n## ++ Added {quantity} {item}(s) at ${price:.2f} each to inventory.")


if __name__ == "__main__":
    display_inventory()
    sell_item("apple", 3)
    sell_item("apple", 10)
    display_inventory()
    add_item("apple", 5, 1.50)
    display_inventory()
    add_item("grape", 8, 2.00)
    display_inventory()
