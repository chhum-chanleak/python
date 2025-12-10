# *1. Syntax errors

# A syntax error means that a program is not valid Python. It doesn't abide by the official rules of the Python language, just like "eat potato good" does not abide by the official rules of the English language.

# Example

# print("Run me!")
# print("Syntax errors mean that the code is not valid Python.")
# print(43 + 31 + 589)
# print(12.43 + 38.43 +)
# print("Can you find the error?")

# *2. Runtime errors

# Runtime errors are sneakier. The computer only discovers these errors as it's running the program, hence the name RUN-time. The program is valid Python syntax, but when the computer actually tries to execute a particular instruction, it gets confused.

# Example

# print("Run me!")
# print("Runtime errors can only be found while the program is running.")
# print(28.32 + 431.89)
# print(47 + "82")
# print("Can you find the error?")

# *3. Logic errors

# Logic errors are a mismatch between what the programmer intended and what the code they wrote actually does. To the computer, these programs seem totally fine. There's nothing wrong with the Python syntax and it understands all of the instructions. When it runs the program, it executes successfully; there is no error message.

# Example

# print("Run me!")
# print("Logic errors are when the program result isn't what you intended.")
# print("The sum of the numbers from 1 to 10 is:")
# print(1 + 2 + 3 + 4 + 5 + 6 + 7 + 9 + 10)
# print("Can you find the error?")

# *4. How can we avoid errors?

# We can't eliminate bugs altogether, but we can program defensively to reduce the amount of time we spend dealing with them.

# 4.1. Iterative development

# The most important strategy is to run our code early and often. Think of this like checkpointing.

# 4.2. Comments

# In Python, any lines of code that start with the # character are treated as comments. When the computer runs a program, it skips over comments entirely. Comments are for humans, not computers!

# 4.3. Pair programming

# Pair programming is an active collaboration where one person types and the other person offers suggestions, switching roles every so often. The person typing talks through their thought process as they go, so the second person can validate what they're doing.