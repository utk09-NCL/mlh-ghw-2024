"""
DICT METHODS

- clear(self): Removes all items from the dictionary.
- copy(self): Returns a shallow copy of the dictionary.
- fromkeys(iterable, value=None): Creates a new dictionary with keys from the iterable and values set to the specified value (or None if not provided).
- get(self, key, default=None): Returns the value for the given key. If the key is not present, returns the default value (or None if not provided).
- items(self): Returns a view object that displays a list of dictionary's key-value tuple pairs.
- keys(self): Returns a view object that displays a list of all keys in the dictionary.
- pop(self, key, default=None): Removes and returns the value for the given key. If the key is not present and a default value is provided, returns the default value. If the key is not present and no default value is provided, raises a KeyError.
- popitem(self): Removes and returns an arbitrary (key, value) pair from the dictionary. Raises a KeyError if the dictionary is empty.
- setdefault(self, key, default=None): Returns the value for the given key. If the key is not present, inserts the key with the default value (or None if not provided) and returns the default value.
- update(self, other_dict): Updates the dictionary with key-value pairs from another dictionary or from an iterable of key-value pairs.
- values(self): Returns a view object that displays a list of all values in the dictionary.
"""

# Create an empty employee dictionary
employee_dict = {}

# Add employees
employee_dict[101] = "Alice"
employee_dict[102] = "Bob"
employee_dict[103] = "Charlie"

# Display the initial dictionary
print("Employee Dictionary:")
print(employee_dict)

# Remove an employee
employee_dict.pop(102, None)

# Display the dictionary after removal
print("\nEmployee Dictionary after removing employee with ID 102:")
print(employee_dict)

# Use other dictionary methods
print("\nKeys View:", employee_dict.keys())
print("Values View:", employee_dict.values())
print("Items View:", employee_dict.items())

# Shallow Copy
employee_dict_copy = employee_dict.copy()
print("\nShallow Copy of Employee Dictionary:")
print(employee_dict_copy)

# fromkeys
new_keys = [104, 105, 106]
new_dict = dict.fromkeys(new_keys, "Unknown")
print("\nNew Dictionary from Keys:")
print(new_dict)

# get
employee_name = employee_dict.get(101, "Employee not found")
print("\nEmployee with ID 101:", employee_name)

# pop
popped_name = employee_dict.pop(103, "Employee not found")
print("\nPopped Employee Name:", popped_name)

# popitem
popped_key_value = employee_dict.popitem()
print("\nPopped (ID, Name) Pair:", popped_key_value)

# setdefault
default_name = employee_dict.setdefault(105, "New Employee")
print("\nDefault Name for ID 105:", default_name)

# update
additional_employees = {107: "David", 108: "Eve"}
employee_dict.update(additional_employees)
print("\nUpdated Employee Dictionary:")
print(employee_dict)

# Clear the dictionary
employee_dict.clear()
print("\nAfter clearing the Employee Dictionary:")
print(employee_dict)
