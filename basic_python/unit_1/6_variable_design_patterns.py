# 1. Referencing a value in multiple places

# Programs may use a value in several different places. We can hardcode that value by just typing it into every place we need it, but if we want to change that value later, we now have to find every place we typed "Shakira" and update it.

# *Do these exercises before advancing.

# Exercise 1: Using +

# Task:
# Create two variables:

# first = "Good"

# second = "Morning"

# Concatenate them (with a space in between) and print:

# Exercise 2: Using +

# Task:
# Create two variables:
# word1 = "Hello"
# word2 = "World"

# 🧩 Exercise 3: Using +

# Task:
# Create two variables:

# first_name = "John"
# last_name = "Doe"

# Exercise 4: Using +

# Task:
# Create two variables:

# day = "Good"
# time = "Evening"

# Bad example

# print("1. You're listening to Shakira")
# print("2. ----------")
# print("3. > Shakira official playlist")
# print("4. > Featuring Shakira")
# print("5. Shakira has 31,234,123 monthly listeners")

# Good example

# singer = "Shakira"
# listeners = "31,234,123"

# print("You're listening to " + singer)
# print("----------")
# print("> " + singer + " official playlist")
# print("> Featuring " + singer)
# print(singer + " has " + listeners + " monthly listeners")

# 2. Reusing a result

# Programs often need to use the result of an operation in multiple places. We can repeat the calculation everywhere we need its result, but if we want to change the calculation later, we need to remember to update every location. If we forget one, we now have a hard-to-find bug where our results are out-of-sync!

# Bad example

# print("Subtotal (including fees):")
# print(41.89 + 41.89 + 41.89 + 2.95 + 3.25 + 3.25 + 3.25)
# print("----------")

# print("Ticket price x3:")
# print(41.89 + 41.89 + 41.89)
# print("Venue fee x3:")
# print(3.25 + 3.25 + 3.25)
# print("Order processing fee:")
# print(2.95)

# Good example
# ticketTotal = 41.89 + 41.89 + 41.89
# venueFee = 3.25 + 3.25 + 3.25
# processingFee = 2.95
# # Demonstrate <ticketTotal + processingFee + venueFee> first before initializing subTotal
# subTotal = ticketTotal + processingFee + venueFee

# print("Subtotal (including fees):")
# print(subTotal)
# print("----------")

# print("Ticket price x3:")
# print(ticketTotal)
# print("Venue fee x3:")
# print(venueFee)
# print("Order processing fee:")
# print(processingFee)

# 3. Generalizing code

# In programming, we want to develop generalized solutions. Maybe we need search results for the term 'python' right now, but our program will be a lot more useful later if it can return search results for any search term. Then, we've not only solved for a single specialized problem, we've solved for a whole class of similar problems.

# Bad example

# print("Your search results are at:")
# print("https://www.khanacademy.org/search?page_search_query=python&content_kinds=Video")

# Good example

# search_term = "python"
# params = "page_search_query=" + search_term + "&content_kinds=Video"

# print("Your search results are at:")
# print("https://www.khanacademy.org/search?" + params)

# 4. Naming variables

# Computers don't understand English, so the actual variable names don't mean anything to them. The computer doesn't care if we name every variable like x1 and x2, or if we store the oldest post in the variable newest_post and the newest post in the variable oldest_post.

# Humans, however, also read programs! For our benefit, a variable name should describe the purpose of that variable, so we can easily understand how it fits into the program.

# Naming rules

# In Python, variable names must follow a few rules.
# Names can contain only letters, numbers, and underscores.
# Names cannot start with a number.
# Names are case-sensitive.
# Names cannot be Python keywords, like print or float.
# By convention, we format Python variable names in snake case. We use all lowercase letters and separate words with underscores, like volume or high_score.

# Naming rules

# In Python, variable names must follow a few rules.
# Names can contain only letters, numbers, and underscores.
# Names cannot start with a number.
# Names are case-sensitive.
# Names cannot be Python keywords, like print or float.

# By convention, we format Python variable names in snake case. We use all lowercase letters and separate words with underscores, like volume or high_score.

# Look out!

# If we access a variable that doesn't exist, we get a NameError. This is a type of runtime error, because the computer only realizes it's stuck when it tries to find the name in its short-term memory and can't.

# NameErrors are often the result of a typo in the variable name. They also happen if we access a variable before it's defined. The first assignment to that variable must execute before any lines of code that access it.

# # Bad example

# first_station = "Pioneer Square"
# print("Now arriving at " + first_station + " station")
# print("Departing " + First_station + " station")
# print("The next station is " + second_station)

# second_station = "International District"
# print("Now arriving at " + secod_station + " station")
# print("Departing " + second_station + " station")
# print("The next station is " + third_station)

# # Good example

# first_station = "Pioneer Square"
# second_station = "International District"
# third_station = "Third station"

# print("Now arriving at " + first_station + " station")
# print("Departing " + first_station + " station")
# print("The next station is " + second_station)


# print("Now arriving at " + second_station + " station")
# print("Departing " + second_station + " station")
# print("The next station is " + third_station)