# 1. Starter built-in functions
# A function is a named set of instructions that performs a task. In general, functions take in one or more input values, perform some operations on them, and then return out an output value.

# A built-in function is just a predefined function created by the developers of Python for us to use. We can find the full list of built-in functions in the official Python docs.

# 2. Function documentation

# To learn how to use a new function, we can look at its documentation. The function documentation tells us the name of the function, the number of input values it takes in, and the output value it returns.

# min(x, y)
# Returns the lesser of the x and y values.

# Programming is not about memorizing hundreds of function names. It's about knowing what kinds of things are possible and where to look! If you forget if it's called min() or minimum(), you can always refer back to the documentation.

# 3. Input and Output
# print(x)

# Displays the value x in the console.

# print("Intro to CS - Python")
# print(93)
# print(4000.25)

# input(x)

# Prompts the user to enter a value.

# Displays x before the prompt

# Always returns a string

# input("Enter your name: ")
# input("Submit (yes/no)? ")
# input(55)        # 55 is shown as the prompt

# 4. Type Casting
# str(x)

# Converts x to a string.
# str(32)       # "32"
# str(12.95)    # "12.95"
# str(-4)       # "-4"

# int(x)

# Converts x to an integer.

# Floats are truncated (decimal removed)

# Invalid strings raise ValueError

# float(x)

# Converts x to a float.

# Invalid strings raise ValueError

# float("18.213")   # 18.213
# float(9)          # 9.0
# float("potato")   # ValueError

# bool(x)

# Converts x to a boolean.

# Rule

# 0, 0.0, "" → False

# Everything else → True

# bool(0)        # False
# bool(43.5)     # True
# bool("False")  # True

# 5. Integers and Floats
# abs(x)

# Returns the absolute value of x.

# Examples

# abs(15)        # 15
# abs(-8)        # 8
# abs(-94.32)    # 94.32

# round(x)

# Rounds x to the nearest integer.

# Uses banker’s rounding (rounds to the nearest even number when exactly .5)

# Examples

# round(3.141)   # 3
# round(3.72)    # 4
# round(3.5)     # 4

# round(x, y)

# Rounds x to y decimal places.

# Examples
# round(6.4368, 1)   # 6.4
# round(6.4368, 2)   # 6.44
# round(6.4368, 3)   # 6.437

# min(x, y, ...)

# Returns the smallest value.

# Can take more than two inputs

# Examples
# min(4, 7)                 # 4
# min(10, -10)              # -10
# min(3, 8, 2, 6)           # 2

# max(x, y, ...)

# Returns the largest value.

# Can take more than two inputs

# Examples
# max(4, 7)                 # 7
# max(1.28, 1.22)           # 1.28
# max(24, 20, 24)           # 24

# 6. Strings
# len(x)

# Returns the number of characters in string x.

# Includes spaces and symbols

# Examples
# len("exit")        # 4
# len("Save as…")    # 10
# len("")            # 0

# min(x, y) (strings)

# Returns the string that comes first in case-sensitive dictionary order.

# Order used
# 0–9  <  A–Z  <  a–z

# Examples
# min("aardvark", "zebra")   # "aardvark"
# min("python", "3")         # "3"
# min("adam", "Adam")        # "Adam"

# max(x, y) (strings)

# Returns the string that comes last in dictionary order.

# Examples
# max("aardvark", "zebra")          # "zebra"
# max("charlie", "Zia")             # "charlie"
# max("word1", "word2", "word3")    # "word3"


# # Rounds to the nearest integer.
# print(round(8.44444444))

# # Rounds to the third decimal place.
# print(round(8.44444444, 3))

# # The bigger negative number is the one closest to 0.
# print(min(-8000, -7000))
# print(str(max(10, 10.5)) + " is bigger.")

# # Has 14 letters, 3 punctuation marks, 3 spaces, and 1 number.
# print(len("Wait, there's 2 more?"))

# # The sort order for symbol characters is non-obvious.
# # It's not super useful to memorize this, though!
# print(min("#khanacademy", "#youcandoanything"))
# print(max("@", "&", "=") + " is bigger.")
# servings=int(input("How many servings per person?"))