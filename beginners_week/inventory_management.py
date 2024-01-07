# Inventory dictionary with items as keys and a tuple of quantity and price as values
inventory = {
    "apple": (10, 1.50),  # (quantity, price)
    "banana": (5, 0.75),
    "orange": (3, 1.25),
}

# Function to display the current inventory
def display_inventory():
    print("\nInventory:")
    for item, (quantity, price) in inventory.items():
        total_cost = quantity * price
        print(
            f">> {item}: {quantity} units at ${price:.2f} each (${total_cost:.2f} total)")

# Function to sell a specified quantity of an item from the inventory
def sell_item(item, quantity):
    print(f"\n## Attempting to sell {quantity} {item}(s)...")
    if item in inventory and quantity <= inventory[item][0]:
        inventory[item] = (inventory[item][0] - quantity, inventory[item][1])
        print(f"\n## -- Sold {quantity} {item}(s).")
    else:
        print(
            f"\n## Cannot sell {quantity} {item}(s). Insufficient stock or item not found.")

# Function to add items to the inventory or update their quantity and average price
def add_item(item, quantity, price):
    if item in inventory:
        # If the item already exists, update the quantity and calculate the new average price
        inventory[item] = (
            inventory[item][0] + quantity, (inventory[item][1] + price) / 2)
    else:
        # If the item is new, add it to the inventory
        inventory[item] = (quantity, price)
    print(
        f"\n## ++ Added {quantity} {item}(s) at ${price:.2f} each to inventory.")


# Display the initial inventory
display_inventory()

# Sell some apples and display the updated inventory
sell_item("apple", 3)
sell_item("apple", 10)
display_inventory()

# Add more apples and display the updated inventory
add_item("apple", 5, 1.50)
display_inventory()

# Add grapes to the inventory and display the final inventory
add_item("grape", 8, 2.00)
display_inventory()
