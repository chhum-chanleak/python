# New

# #py0ak

# Exercises: Tracing variables

# What are the outputs?

# 1.
# fruit = "apple"
# sum = 4 + 5 + 2

# print(fruit + "fruit")

# sum = sum + 1
# fruit = sum
# sum = fruit + 5

# print(sum + fruit)

# 2.
# name = "banana"
# count = 3 + 7

# print(name + " pie")

# count = count + 2
# name = count
# count = name + 10

# print(count + name)

# 3.

# city = "Paris"
# total = 5 + 8

# print("Visit " + city)

# total = total * 2
# city = total
# total = city + 3

# print(total + city)

# 4.
# animal = "cat"
# score = 7 + 1

# print(animal + "s are cute")

# score = score - 2
# animal = score
# score = animal * 2

# print(score + animal)

# Do exercises of "Trace variables" at https://www.khanacademy.org/computing/intro-to-python-fundamentals/x5279a44ae0ab15d6:computational-thinking-with-variables/x5279a44ae0ab15d6:variables/e/tracing-variables

#py0an

# Exercises: input()

# 1.
client = input("Enter client name: ")
caterer = "King Catering"

message = caterer + " will serve " + client

print("Catering Contract (" + caterer + ")")
print("----------")
print(message)

# a.
# What value is stored in client if the user types: Dara
# b.
# What is the value of the variable caterer?
# c.
# What is stored in the variable message after the code runs
# (assume the user typed Dara)?
# d.
# What is the exact output printed to the screen?

# 2.
# event = input("Enter event name: ")
# organizer = "Elite Events"

# info = organizer + " is organizing " + event

# print("Event Information")
# print("----------")
# print(info)

# a.
# What value is stored in event if the user types: Wedding
# b.
# What is the value of organizer?
# c.
# What is stored in info after the code runs?
# d.
# What is the exact output printed?

# 3.
# customer = input("Enter customer name: ")
# service = "Cleaning Service"

# statement = service + " provided to " + customer

# print("Service Agreement")
# print("----------")
# print(statement)

# a.
# What value is stored in customer if the user types: Jin
# b.
# What is the value of service?
# c.
# What is stored in statement?
# d.
# What is the exact output printed?

# 4.
# student = input("Enter student name: ")
# course = "Python Basics"

# enrollment = student + " enrolled in " + course

# print("Course Enrollment")
# print("----------")
# print(enrollment)

# a.
# What value is stored in student if the user types: Sarah
# b.
# What is the value of course?
# c.
# What is stored in enrollment?
# d.
# What is the exact output printed?

#py0ao

# Do challenge: URL paths at https://www.khanacademy.org/computing/intro-to-python-fundamentals/x5279a44ae0ab15d6:computational-thinking-with-variables/x5279a44ae0ab15d6:program-execution/pc/pair-programming

# Due

# Exercise 1: Name basic comparison operators. What type of value/object do these operators generate?
# Exercise 2: Logical Operators (and)
# Task: A user must be at least 18 years old and have a valid ID to access a feature. Create two boolean variables, is_adult and has_id. Use the logical and operator to determine if the user is eligible. Store the result in is_eligible and print it.
# is_adult = True
# has_id = False

# Exercise 3: (OR Version): Logical Operators (or)
# Task:
# A user can access a feature if they are at least 18 years old or they have a special permission. Create two boolean variables, is_adult and has_permission. Use the logical or operator to determine if the user is eligible. Store the result in is_eligible and print it.

# # Variables
# is_adult = True
# has_permission = False

# Exercise 4: Comparison Operators
# Task: Create two integer variables, temp_celsius and max_safe_temp. Use a comparison operator to determine if temp_celsius is greater than max_safe_temp. Store the result in a boolean variable named is_overheating and print its value.
# temp_celsius = 95
# max_safe_temp = 90

#py0am

# 1.
# name = input("Enter your name: ")
# print(name)
# What will be printed if the user types: Alex

# 2.
# x = input("Enter something: ")
# print(type(x))
# What is printed, no matter what the user types?

# 3.
# a = input("Enter first number: ")
# b = input("Enter second number: ")
# print(a + b)
# If the user enters: 3, 4
# What will be printed?

# 4.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print(a + b)
# If the user enters: 3, 4
# What will be printed?

#py0ai

# Exercise 1: Check Positive Number
# Task:
# Write a program that checks whether a number is positive or not.
# Create a variable num and assign any integer.
# Use a conditional (if-else) to print:
# "Positive number" if the number is greater than 0
# "Not positive" otherwise
# Test case idea: Try num = -3 and num = 10.

# Exercise 2: Check Even or Odd
# Task:
# Write a program that determines if a number is even or odd.
# Create a variable num and assign any integer.
# Use a conditional to check:
# "Even number" if divisible by 2
# "Odd number" otherwise
# Test case idea: Try num = 7 and num = 12.

# Exercise 3: Grade Check
# Task:
# Write a program that prints a letter grade based on a numeric score.
# Create a variable grade with a value between 0–100.
# Use if-elif-else to print:
# "A grade" if grade ≥ 90
# "B grade" if grade ≥ 80
# "C or below" otherwise
# Test case idea: Try grade = 92, grade = 85, and grade = 70.

# Exercise 4: Age Restriction
# Task:
# Write a program that checks if someone can vote.
# Create a variable age.
# Print:
# "You can vote" if age ≥ 18
# "Too young to vote" otherwise
# Test case idea: Try age = 17 and age = 21.