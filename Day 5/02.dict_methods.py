a = {
    "Harry" : 100,
    "Sam" : 45,
    "Sai" : 56,
    "List" : [5,4,56,2]
}

print(a.items())  # Returns the (key:value) pairs
print(a.keys())  # Retrurn the Key only.
print(a.values())   # Return the Values only.
print(a.update({"Harry" : 50}, {"Sundar" : 99}))   # Updates the intial key value if present in the dict, and if key is not present in the dict it adds it to the existing Dictonary.

print(a.get("Harry"))   # Return the value if existed. If value is not present it return "NONE".. {Don't retuns the Error}

print(a.get("Sam")) # Return 'NONE'....!
print(a["Sam"]) # It retunrs the error, because 'Sam' dosen't present into the DICTONARY...


# Additional Methods : 

