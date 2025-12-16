# Exercise 2: Slicing and Indexing
# Task: Use the string language = "Python". Extract and print the first letter using indexing and the last three letters using slicing.

language = "Python"

# Single letter indexing                    -2 -1 0 1 2

n = language[-1]
o = language[-2]

# print(o)

# print(language[0])
# print(language[1])

# print(language[-1])
# print(language[-2])

# Basic slicing

# Slice at "t"
# "Python"

py = language[0:2]
pyth = language[0:4]
yth = language[1:4]

# print(yth)

# print(language[0:2])

# Slice from the beginning
python = language[:]

# print(python)

# print(language[0:4])
# print(language[:4])

# Slice to the end

# print(language[0:])

# Slice with a step

print(language[0::2])      # "Python"

# print(language[0:-1:2])

print("Lim Lysean"[:-1:2]) # Lim Lysean # LmLsa
