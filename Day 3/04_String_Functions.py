# Python provides the String functions to perform operations on string.

# 1. len() returns the length of the string
str = "India"
print(len(str)) # Output : 5

# 2. endswith() checks if a string ends with given text
str = "India"
print(str.endswith("ia")) # Output : True

# 3. count() counts total occurrences of a character
str = "india"
print(str.count("i")) # Output : 2

#4. capitalize() capitalizes the first character.
str = "india"
print(str.capitalize()) # Output : India

# 5. find() returns the index of first occurrence
str = "India"
print(str.find("a")) # Output : 4

# 6. replace(old word, new word) replaces the old word with the new word in the string.
str = "India"
print(str.replace("India", "England"))