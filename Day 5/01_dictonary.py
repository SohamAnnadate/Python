# Dictonary is a combination of Key and Values [key : value]
# Rules : 
"""
    1. It is mutable.
    2. It is Indexed.
    3. It is Unordered
    4. Cannot Contains Duplicate Keys.
"""

a = {}    # Empty Dictonary
print(type(a))

b = {
    "Harry" : 100,
    "Sam" : 45,
    "Sai" : 56,
    "List" : [5,4,56,2]
}

# print(b["Key"])  # Output should always return Value
print(b["Harry"])
print(b['List'])
print(b)


