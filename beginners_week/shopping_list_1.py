"""
LIST METHODS

- append(self, item): Appends an item to the end of the list.
- clear(self): Removes all items from the list.
- copy(self): Returns a shallow copy of the list.
- count(self, item): Returns the number of occurrences of the item in the list.
- extend(self, iterable): Appends the elements of an iterable to the end of the list.
- index(self, item, start=0, end=-1): Returns the index of the first occurrence of the item in the list.
- insert(self, index, item): Inserts an item at a specific index in the list.
- pop(self, index=-1): Removes and returns the item at the specified index. If no index is specified, removes and returns the last item.
- remove(self, item): Removes the first occurrence of the item from the list.
- reverse(self): Reverses the order of the items in the list.
- sort(self, key=None, reverse=False): Sorts the items of the list in ascending order. Optional parameters key and reverse can be used to customize the sorting.
"""

# Create an empty shopping list
shopping_list = []

# Append items to the list
shopping_list.append("Apple")
shopping_list.append("Apple")
shopping_list.append("Banana")
shopping_list.append("Orange")
print("After appending items:", shopping_list)

# Count occurrences of an item
count_apple = shopping_list.count("Apple")
print("Number of 'Apple' in the shopping list:", count_apple)

# Extend the list with another iterable
more_items = ["Milk", "Bread", "Cheese"]
shopping_list.extend(more_items)
print("After extending with more items:", shopping_list)

# Get the index of an item
index_banana = shopping_list.index("Banana")
print("Index of 'Banana' in the shopping list:", index_banana)

# Insert an item at a specific index
shopping_list.insert(1, "Grapes")
print("After inserting 'Grapes' at index 1:", shopping_list)

# Pop an item from the list
popped_item = shopping_list.pop(2)
print(f"Popped item at index 2: {popped_item}, Updated list:", shopping_list)

# Remove an item from the list
shopping_list.remove("Orange")
print("After removing 'Orange':", shopping_list)

# Reverse the order of items
shopping_list.reverse()
print("After reversing the shopping list:", shopping_list)

# Sort the list in ascending order
shopping_list.sort()
print("After sorting in ascending order:", shopping_list)

# Clear the list
shopping_list.clear()
print("After clearing the shopping list:", shopping_list)

print("\n\n")
# Shallow copy with nested lists
original_list = [1, [2, 3], [4, 5]]
shallow_copied_list = original_list.copy()

# Shallow copy (copy()) creates a new list with new references to the same objects inside the list. However, since integers are immutable, modifying an integer creates a new integer object, and it doesn't affect the original list.
# If the list contained mutable objects (like lists), modifying those mutable objects would be reflected in both the original and the copied list, as they would reference the same nested objects.

# Modify an element in the nested list
original_list[1][0] = 99
shallow_copied_list[2][0] = 77

print("Original List:\t\t", original_list)
print("Shallow Copied List:\t", shallow_copied_list)
print("\n")

# print(dir(str))
