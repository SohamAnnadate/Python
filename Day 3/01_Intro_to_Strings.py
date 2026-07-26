# String is a datatype in a python.
# String is a sequence of characters enclosed in quotes.
# We can primarily write a string in three ways.

a = "Soham"
b = 'Sam'
c = '''My name is soham'''

print(a)
print(b)
print(c) 

# String Slicing.....

# A string in python can be scliced for getting a part of the strings.

# [ S  O  H  A  M ]  #String Characters
# [ 0  1  2  3  4 ]  #from 0 to len-1
# [-5 -4 -3 -2 -1]   #from negative numbers form last to first

name = "SohamAnnadate"
name2 = name[0:6] # trims the string from 0th index to the 6th index (excluding 6th index).
print(name2)