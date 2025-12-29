#py0u

# Exercise: Identifying Python Errors

# 1.
# num = 6

# if (num % 2) == 1:
#     print("Number is odd")
# else:
#     print("Number is even")

# # 2.
# print("Welcome to Python!")

# 3.
# x = 10
# y = 0
# print(x / y)

# 4.
# numbers = [1, 2, 3]
# print(numbers[3])

# 5.
# if 5 > 3:
    # print("Five is greater than three")

#py0h

# 1.
# CODE WITH ERROR
# original_price = 50.0
# discount_rate = 0.10 # 10%
# discount_amount = original_price * discount_rate
# discounted_price = original_price - discount_amount

# print(discounted_price)

# # This calculates the discount amount, but doesn't subtract it.
# final_price = original_price - discount_amount

# print(f"Original: ${original_price}")
# print(f"Calculated Final Price: ${final_price}")
# Current Output: Calculated Final Price: $5.0 (INCORRECT)

# 2.
# CODE WITH ERROR
# total_score = 85
# num_subjects = 4

# Uses integer division (//) instead of float division (/)
# average_grade = total_score // num_subjects

# print(f"Total Score: {total_score}")
# print(f"Calculated Average Grade: {average_grade}")
# Current Output: Calculated Average Grade: 17 (INCORRECT for a precise average)
# Solution Goal: Modify the average_grade line so the output is 17.0.

# 3. What type of errors are these?
# These are logic errors.

#py0v
# Have one student predict the output first.
# Run the code and observe differences.
# Discuss the error (prin) and how Python identifies it.
# Discuss type differences: "2" + "5" is string concatenation vs 8 / 2 is numeric division.

# ============================================
# Pair Programming: Evaluating Expressions
# ============================================

# print("Evaluating string expressions...")

# # What does each string expression evaluate to?
# print("hello" + " world") 
# print("data" + "_" + "science")
# print("AI" + " " + "tools")
# print(2 + 5 + 8.3)

# # Display a divider surrounded by blank lines
# print()
# print("==========")
# print()

# print("Evaluating integer and float expressions...")

# # What does each numeric expression evaluate to?
# print(10 + 5)
# print(3.5 + 2.5)
# print(-7 + 0.33)
# print(8 / 2)  # test float division

#py0x

# Exercises: Assignments and initialization

# 1. Create a variable city and assign it "Singapore". Print it.

# 2. Create two variables a = 7 and b = 3. Print their sum.

# 3. Reassign the value of a to 10 and print the new sum with b.

# 4. Create a variable is_hungry and assign it True. Print it.

#py0a

# 1.
# CODE WITH ERROR
# We have three separate variables
# point1 = 10
# point2 = 20
# point3 = 30

# The code attempts to access a fourth point, which doesn't exist
# fourth_point = point4
# print(fourth_point)

# 2.
# # CODE WITH ERROR
# # Attempting to add a string and an integer
# text = "Result is: "
# number = 100
# final_output = text + number
# print(final_output)

# 3. What type of errors are these?

# Exercises: Naming

# 1.
# first_station = "Pioneer Square"
# second_station = "International District"
# third_station = "Final station"

# print("Now arriving at " + first_station + " station")
# print("Departing " + first_station + " station")
# print("The next station is " + second_station)

# print("Now arriving at " + second_station + " station")
# print("Departing " + second_station + " station")
# print("The next station is " + third_station)

# 2.
# city = "Seattle"
# print("Welcome to " + city_name)

# 3.
# if (3 < 0)
#   message = "Hello, world!"

# print(message)

# What types of errors are all of these?