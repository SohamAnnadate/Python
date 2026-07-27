# Unlike Strings, Python also Provides the methods for Lists.

l1 = ["Sam", "Ram", "Sai", "Seeta", 5, 5.125, True]
l2 = [5, 58, 1, 154, 23]

l2.sort()
print(l2)

l1.reverse()
print(l1)

# Python List Methods

# 1. append() adds an element at the end of the list
lst = [10, 20, 30]
lst.append(40)
print(lst)   # Output : [10, 20, 30, 40]

# 2. extend() adds multiple elements to the end of the list
lst = [10, 20]
lst.extend([30, 40])
print(lst)   # Output : [10, 20, 30, 40]

# 3. insert() inserts an element at a specified index
lst = [10, 20, 30]
lst.insert(1, 15)
print(lst)   # Output : [10, 15, 20, 30]

# 4. remove() removes the first occurrence of the specified element
lst = [10, 20, 30, 20]
lst.remove(20)
print(lst)   # Output : [10, 30, 20]

# 5. pop() removes and returns the element at the specified index
lst = [10, 20, 30]
print(lst.pop(1))   # Output : 20
print(lst)          # Output : [10, 30]

# 6. clear() removes all elements from the list
lst = [10, 20, 30]
lst.clear()
print(lst)   # Output : []

# 7. index() returns the index of the first occurrence of an element
lst = [10, 20, 30]
print(lst.index(20))   # Output : 1

# 8. count() returns the number of occurrences of an element
lst = [10, 20, 20, 30]
print(lst.count(20))   # Output : 2

# 9. sort() sorts the list in ascending order
lst = [30, 10, 20]
lst.sort()
print(lst)   # Output : [10, 20, 30]

# 10. reverse() reverses the order of the list
lst = [10, 20, 30]
lst.reverse()
print(lst)   # Output : [30, 20, 10]

# 11. copy() returns a copy of the list
lst = [10, 20, 30]
new_lst = lst.copy()
print(new_lst)   # Output : [10, 20, 30]

# ✅ Built-in functions commonly used with lists

# len() returns the number of elements
lst = [10, 20, 30]
print(len(lst))   # Output : 3

# max() returns the largest element
lst = [10, 20, 30]
print(max(lst))   # Output : 30

# min() returns the smallest element
lst = [10, 20, 30]
print(min(lst))   # Output : 10

# sum() returns the sum of all elements
lst = [10, 20, 30]
print(sum(lst))   # Output : 60

# sorted() returns a new sorted list
lst = [30, 10, 20]
print(sorted(lst))   # Output : [10, 20, 30]


# Note: Python lists have 11 built-in methods:
# append(), extend(), insert(), remove(), pop(), clear(), index(), count(), sort(), reverse(), and copy(). The functions like len(), max(), min(), sum(), and sorted() are built-in functions, not list methods.