#py0i

# Exactly. You've got it—an if...else (or if...elif...else) block is like a one-way gate. It stops the moment it finds a condition that is True.

# Even if there are five other conditions later in the code that are also true, Python will never see them because it "exits" the entire block as soon as the first match is made.

# Use pens and paper for efficiency

# if = a tree with one branch 

# Example 1: Check Positive Number

# num = -1

# if (num > 0): # true
#   print("Num is positive.")
# elif (num == 5): # true
#   print("Num is 0")
      
# if (num == 2): # false
#   print("Num is 2")
# else:
#   print("Hi")

# Example 2: Check Even or Odd

# num = 3

# if (num % 2) == 0:
#   print("Even number")
# else:
#   print("Odd number")

# Example 3: Grade Check

# grade = 85

# if grade >= 90:
#     print("A grade")
# elif grade >= 80:
#     print("B grade")
# else:
#     print("C or below")

# Example 4: Age Restriction

# age = 17

# if age >= 18:
#   print("You can vote")
# else:
#   print("Too young to vote")

#py0ai
# Exercise 1: Check Positive Number

# Task:
# Write a program that checks whether a number is positive or not.
# Create a variable num and assign any integer.
# Use a conditional (if-else) to print:
# "Positive number" if the number is greater than 0
# "Not positive" otherwise
# Test case idea: Try num = -3 and num = 10.

# num = 10

# if (num > 0):
#   print("Positive number.")
# else:
#   print("Not positive")

#py0aj
# Exercise 2: Check Even or Odd
# Task:
# Write a program that determines if a number is even or odd.
# Create a variable num and assign any integer.
# Use a conditional to check:
# "Even number" if divisible by 2
# "Odd number" otherwise
# Test case idea: Try num = 7 and num = 12.

# num = 12

# if (num % 2) == 0:
#   print("Even number.")
# else:
#   print("Odd number.")

#py0ak

# Exercise 3: Grade Check
# Task:
# Write a program that prints a letter grade based on a numeric score.
# Create a variable grade with a value between 0–100.
# Use if-elif-else to print:
# "A grade" if grade ≥ 90
# "B grade" if grade ≥ 80
# "C or below" otherwise
# Test case idea: Try grade = 92, grade = 85, and grade = 70.

#py0al
# Exercise 4: Age Restriction
# Task:
# Write a program that checks if someone can vote.
# Create a variable age.
# Print:
# "You can vote" if age ≥ 18
# "Too young to vote" otherwise
# Test case idea: Try age = 17 and age = 21.

#py0s
# Exercise 1: Concatenation and Length
# Task: Create two string variables, first_name and last_name. Concatenate them with a space in between to form full_name. Then, calculate and print the length of full_name.

# first_name = "Alan"
# last_name = "Turing"
 
#py0a

# 0. Learn basic array first before attempting exercise number 1.

# A list is an ordered, mutable collection of items in python.

# Example 1: Creating a list

# numbers = [4, 3, 2, 1]

# print(numbers)

# Example 2: Accessing/indexing/extracting elements

# fruits = ["apple", "banana", "cherry"]
# print(fruits[2])  # number 2 here is called an "index"
# print(fruits[0])  # number 0 here is called an "index"

# Example 3: Modifying a list (mutable)

# colors = ["red", "blue", "green"]

# colors[1] = "yellow"
# print(colors)

# Example 4: Adding elements

# animals = ["cat", "dog"]

# animals.append("elephant")
# print(animals)

#py0ad
# Exercise 1: Creating a list
# Task:
# Create a list called scores that contains these numbers in order:
# 10, 20, 30, 40
# Then print the list.
# 👉 Goal: Get comfortable writing a list literal.

#  Exercise 2: Accessing (indexing) elements

# names = ["Alice", "Bob", "Charlie"]

# Task:
# Print "Bob" using its index
# Print "Alice" using its index

# Exercise 3: Modifying a list

# cities = ["Paris", "London", "Tokyo"]

# Task:
# Change "London" to "Berlin" and print the updated list.

# Exercise 4: Adding elements

# numbers = [1, 2, 3]

# Task:
# Add the number 4 to the end of the list, then print the list.

# 1.
# # CODE WITH ERROR
# data_points = [10, 20, 30]
# # List indices are 0, 1, 2. The code attempts to access the 4th element (index 3).
# fourth_point = data_points[3]
# print(fourth_point)

# 2.
# # CODE WITH ERROR
# # Attempting to add a string and an integer
# text = "Result is: "
# number = 100
# final_output = text + number
# print(final_output)

# 3. What type of errors are these?

#py0u
# Exercise 2: Calculating Area of a Circle
# Task: Use the value 3.14159 for Pi and store it in a float variable. Given a radius of 5.5, calculate the area of the circle using the formula $= pi * r^2. Print the result.

# # pi = 3.14159
# # radius = 5.5

#py0h

# 1.
# # CODE WITH ERROR
# original_price = 50.0
# discount_rate = 0.10 # 10%

# # Logic Bug: This calculates the discount amount, but doesn't subtract it.
# final_price = original_price * discount_rate

# print(f"Original: ${original_price}")
# print(f"Calculated Final Price: ${final_price}")
# # Current Output: Calculated Final Price: $5.0 (INCORRECT)

# 2.
# # CODE WITH ERROR
# total_score = 85
# num_subjects = 5

# # Logic Bug: Uses integer division (//) instead of float division (/)
# average_grade = total_score // num_subjects

# print(f"Total Score: {total_score}")
# print(f"Calculated Average Grade: {average_grade}")
# # Current Output: Calculated Average Grade: 17 (INCORRECT for a precise average)
# # Solution Goal: Modify the average_grade line so the output is 17.0.

# 3. What type of errors are these?

#py0b

# 1. In programming, what is another word for "bugs"?
# 2. What is another words for "debugging"?

#py0k

# Exercise: Fix and identify errors/bugs

# 1.
# print("Monthly Financial Summary")
# print("October 2025")
# # The closing quote is missing for the dashed line
# print("----
# print("---")

# # Rent and utilities
# print("Operational Costs:")
# print(800.00 + 150.75 + 45.10)

# 2.
# Report on weekly tasks completed.

# print("Team Project Status")
# print("Week 4 Tasks")

# This line attempts to print the result of an arithmetic operation,
# but uses the print function inside the arithmetic.
# print(4 + print(5))

# 3.
# print("Q1 Revenue Report")

# # Define quarterly revenue figures
# Q1_revenue = 120000

# # An attempt is made to print the variable name incorrectly
# print(q1 revenue)

# # Incorrect statement and mismatched quotes
# print('Quarterly Sales Data")

# 4.
# # Printing a short log message

# print("Server Log:")

# # Missing closing parenthesis and string quote
# print("Connection established at 14:30
#   print("Status: OK") # This line has incorrect indentation

# #py0ab

# Exercise 4: Exponential and Negative Numbers
# Task: Calculate the result of negative five raised to the power of three. Store the result in a variable and print it. Use the exponentiation operator (**).

#py0n

# Do challenge "Pair programming" at https://www.khanacademy.org/computing/intro-to-python-fundamentals/x5279a44ae0ab15d6:computational-thinking-with-variables/x5279a44ae0ab15d6:program-execution/pc/pair-programming

#py0aa
# Exercise 3: Type Conversion
# Task: You are given a variable count_str that is currently a string. Convert this string variable into an integer and then increment its value by 1. Print the final result.

# count_str = "99"

#py0t
# Exercise 2 (OR Version): Logical Operators (or)
# Task:
# A user can access a feature if they are at least 18 years old or they have a special permission. Create two boolean variables, is_adult and has_permission. Use the logical or operator to determine if the user is eligible. Store the result in is_eligible and print it.

# # Variables
# is_adult = True
# has_permission = False

#py0q

# Exercise 1: Basic Float Operations
# Task: Create two float variables, price and tax_rate. Calculate the total tax amount and the final total cost (price + tax). Print both results rounded to two decimal places.

# price = 49.99
# tax_rate = 0.075

#py0y

# Exercise 3: Case Conversion and Checking
# Task 1: Given the string phrase = "tHis Is A TesT", convert it entirely to lowercase. Then, use a string method to check if the original string starts with the letter 't' (case-sensitive).
# Task 2: Given the string greeting = "hElEo, WoRlD!", convert it entirely to uppercase. Then, use a string method to check if the last letter of the original string ends with the letter ''D" (case-sensitive).

# ============================================
# Pair Programming: Evaluating Expressions
# ============================================

# print("Evaluating string expressions...")

# # What does each string expression evaluate to?
# print("hello" + " world")
# print("data" + "_" + "science")
# prin("AI" + " " + "tools")  # intentional typo to discuss error
# print("2" + "5" + "8.3")

# # Display a divider surrounded by blank lines
# print()
# print("==========")
# print()

# print("Evaluating integer and float expressions...")

# # What does each numeric expression evaluate to?
# print(10 + 5)
# print(3.5 + 2.5)
# print(100)
# print(-7 + 0.33)
# print(8 / 2)  # test float division