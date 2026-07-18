import os

# Specify the directory path
#  " . " represents the current directory
#  " path " represents the specific directory

path = "/"

# Print the contents of the directory
contents = os.listdir(path)

print("Contents of the directory:")
for item in contents:
    print(item)