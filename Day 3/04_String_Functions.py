# Python provides many String functions (methods) to perform operations on strings.

# 1. len() returns the length of the string
str = "India"
print(len(str))   # Output : 5


# 2. endswith() checks if a string ends with the given text
str = "India"
print(str.endswith("ia"))   # Output : True


# 3. startswith() checks if a string starts with the given text
str = "India"
print(str.startswith("In"))   # Output : True


# 4. count() counts the total occurrences of a character or substring
str = "India"
print(str.count("i"))   # Output : 1


# 5. capitalize() capitalizes the first character
str = "india"
print(str.capitalize())   # Output : India


# 6. title() capitalizes the first letter of every word
str = "hello world"
print(str.title())   # Output : Hello World


# 7. upper() converts all characters to uppercase
str = "India"
print(str.upper())   # Output : INDIA


# 8. lower() converts all characters to lowercase
str = "India"
print(str.lower())   # Output : india


# 9. swapcase() converts uppercase to lowercase and vice versa
str = "InDiA"
print(str.swapcase())   # Output : iNdIa


# 10. strip() removes spaces from both ends
str = "   India   "
print(str.strip())   # Output : India


# 11. lstrip() removes spaces from the left side
str = "   India"
print(str.lstrip())   # Output : India


# 12. rstrip() removes spaces from the right side
str = "India   "
print(str.rstrip())   # Output : India


# 13. find() returns the index of the first occurrence
str = "India"
print(str.find("a"))   # Output : 4


# 14. index() returns the index of the first occurrence
str = "India"
print(str.index("d"))   # Output : 2


# 15. replace(old, new) replaces the old text with the new text
str = "India"
print(str.replace("India", "England"))   # Output : England


# 16. split() splits the string into a list
str = "Python Java C++"
print(str.split())   # Output : ['Python', 'Java', 'C++']


# 17. join() joins list elements into a string
list1 = ["Python", "Java", "C++"]
print(" - ".join(list1))   # Output : Python - Java - C++


# 18. isalpha() checks whether all characters are alphabets
str = "India"
print(str.isalpha())   # Output : True


# 19. isdigit() checks whether all characters are digits
str = "12345"
print(str.isdigit())   # Output : True


# 20. isalnum() checks whether all characters are alphabets or digits
str = "India123"
print(str.isalnum())   # Output : True


# 21. isspace() checks whether all characters are spaces
str = "     "
print(str.isspace())   # Output : True


# 22. casefold() converts the string to lowercase (more aggressive than lower())
str = "HELLO"
print(str.casefold())   # Output : hello
