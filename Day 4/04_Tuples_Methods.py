# Python tuples are immutable, so they have only two built-in methods.

# Python Tuple Methods

# 1. count() returns the number of occurrences of an element
tup = (10, 20, 30, 20, 40)
print(tup.count(20))   # Output : 2

# 2. index() returns the index of the first occurrence of an element
tup = (10, 20, 30, 40)
print(tup.index(30))   # Output : 2


# ✅ Common Built-in Functions Used with Tuples

# len() returns the number of elements
tup = (10, 20, 30)
print(len(tup))   # Output : 3

# max() returns the largest element
tup = (10, 20, 30)
print(max(tup))   # Output : 30

# min() returns the smallest element
tup = (10, 20, 30)
print(min(tup))   # Output : 10

# sum() returns the sum of all elements
tup = (10, 20, 30)
print(sum(tup))   # Output : 60

# sorted() returns a sorted list
tup = (30, 10, 20)
print(sorted(tup))   # Output : [10, 20, 30]

# Note: Tuples have only 2 methods because they are immutable:
# count()
# index()