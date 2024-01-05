# Original string
og_str = "HI, Welcome to GHW"
print("Original String:", og_str)

"""
Case Modification Methods:
- capitalize(): Returns a copy of the string with its first character capitalized.
- casefold(): Returns a casefolded copy of the string, suitable for case-insensitive comparisons.
- lower(): Returns a copy of the string converted to lowercase.
- upper(): Returns a copy of the string converted to uppercase.
- swapcase(): Returns a copy of the string with uppercase characters converted to lowercase and vice versa.
- title(): Returns a titlecased version of the string, where words start with an uppercase character and the remaining characters are lowercase.
"""
# Case Modification
print(og_str.capitalize())
print(og_str.casefold())
print(og_str.lower())
print(og_str.upper())
print(og_str.swapcase())
print(og_str.title())

"""
Alignment and Formatting Methods:
- center(width, fillchar): Returns a centered string of a specified width with optional fill characters.
- ljust(width, fillchar): Returns a left-justified string of a specified width with optional fill characters.
- rjust(width, fillchar): Returns a right-justified string of a specified width with optional fill characters.
- zfill(width): Returns a copy of the string padded with zeros on the left to achieve the specified width.
"""
# Alignment and Formatting
print(og_str.center(30, '*'))
print(og_str.ljust(30, '*'))
print(og_str.rjust(30, '*'))
print(og_str.zfill(30))

"""
Searching and Counting Methods:
- count(substring, start, end): Returns the number of occurrences of a substring in the given range.
- endswith(suffix, start, end): Returns True if the string ends with the specified suffix.
- find(substring, start, end): Returns the lowest index of a substring or -1 if not found.
- index(substring, start, end): Returns the lowest index of a substring or raises a ValueError if not found.
- rfind(substring, start, end): Returns the highest index of a substring or -1 if not found.
- rindex(substring, start, end): Returns the highest index of a substring or raises a ValueError if not found.
"""
# Searching and Counting
print(og_str.count('e'))
print(og_str.endswith('GHW'))
print(og_str.find('Welcome'))
print(og_str.index('Welcome'))
print(og_str.rfind('e'))
print(og_str.rindex('e'))


"""
Transformation and Modification Methods:
- expandtabs(tabsize): Expands tabs in the string to multiple spaces.
- join(iterable): Joins the elements of an iterable (e.g., a list) into a single string.
- replace(old, new, count): Replaces occurrences of a substring with another substring, optionally up to a specified count.
- removeprefix(prefix): Removes a specified prefix from the start of the string.
- removesuffix(suffix): Removes a specified suffix from the end of the string.
"""
# Transformation and Modification
tabbed_str = "Hello\tWorld"
print(tabbed_str.expandtabs(4))

words = ["Hello", "World"]
print('-'.join(words))

prefix_str = "HelloWorld"
print(prefix_str.removeprefix("Hello"))

suffix_str = "HelloWorld"
print(suffix_str.removesuffix("World"))

"""
Splitting and Joining Methods:
- split(sep, maxsplit): Splits the string into a list of substrings using a specified separator.
- rsplit(sep, maxsplit): Splits the string into a list of substrings, starting from the right.
- splitlines(keepends): Splits the string at line breaks and returns a list of lines.
- partition(sep): Splits the string at the first occurrence of a specified separator and returns a tuple.
- rpartition(sep): Splits the string at the last occurrence of a specified separator and returns a tuple.
"""
# Splitting and Joining
print(og_str.split(' '))
print(og_str.rsplit(' '))
multiline_str = "Line 1\nLine 2\nLine 3"
print(multiline_str.splitlines())
print(og_str.partition('Welcome'))
print(og_str.rpartition('Welcome'))


"""
Other Utility Methods:
- encode(encoding, errors): Encodes the string using a specified encoding.
- expandtabs(tabsize): Expands tabs in the string to multiple spaces.
- isspace(): Returns True if all characters in the string are whitespace.
- istitle(): Returns True if the string - is a titlecased string.
- isalnum(): Returns True if all characters in the string are alphanumeric.
- isalpha(): Returns True if all characters in the string are alphabetic.
- isascii(): Returns True if all characters in the string are ASCII.
- isdecimal(): Returns True if all characters in the string are decimals.
- isdigit(): Returns True if all characters in the string are digits.
- isidentifier(): Returns True if the string - is a valid identifier.
- islower(): Returns True if all cased characters in the string are lowercase.
- isnumeric(): Returns True if all characters in the string are numeric.
- isprintable(): Returns True if all characters in the string are printable.
- isspace(): Returns True if all characters in the string are whitespace.
- startswith(prefix, start, end): Returns True if the string starts with the specified prefix.
- strip([characters]): Returns a copy of the string with leading and trailing characters removed.
- lstrip([characters]): Returns a copy of the string with leading characters removed.
- rstrip([characters]): Returns a copy of the string with trailing characters removed.
- translate(table): Returns a copy of the string where each character is mapped through the given translation table.
- center(width, fillchar): Returns a centered string of a specified width with optional fill characters.
- ljust(width, fillchar): Returns a left-justified string of a specified width with optional fill characters.
- rjust(width, fillchar): Returns a right-justified string of a specified width with optional fill characters.
- startswith(prefix, start, end): Returns True if the string starts with the specified prefix.
"""

# Other Utility Methods
print(og_str.encode())
print(og_str.isspace())
print(og_str.istitle())
print(og_str.isalnum())
print(og_str.isalpha())
print(og_str.isascii())
print(og_str.isdecimal())
print(og_str.isdigit())
print(og_str.isidentifier())
print(og_str.islower())
print(og_str.isnumeric())
print(og_str.isprintable())
print(og_str.isspace())
print(og_str.startswith('HI'))
print(og_str.strip())
print(og_str.lstrip())
print(og_str.rstrip())

# Define trans_table for translation methods
trans_table = str.maketrans('HW', '12')
print(og_str.translate(trans_table))
