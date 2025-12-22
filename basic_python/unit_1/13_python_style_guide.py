# Mastering programming isn't just about writing code that works. A great programmer also writes code that's easy to use and understand!

# Code readability

# We should be able to get a high-level understanding of what a program does at a glance. We call this a readable program.

# Readability has no impact on the computer's ability to understand a program. It's for the benefit of humans only, whether that's our future selves or other programmers. We spend time making our code readable now, so we can spend less time deciphering our code when we try to use, modify, or debug it later.

# Formatting
# ifi Wrote this_article likeThis , u could pbly UnderstandWhatI .wrote ,but IT would takeyou a lot_longertoRead
# It's the same for programs! Formatting code in a standard way makes it easier for us to read. As our brains learn to expect a certain format, they can scan the code more quickly to get to the meaning.

# Naming and documentation

# What do you think this program calculates?

# num1 = 2
# num2 = 4
# print(num1 * 3 + num2)

# It could be anything! Descriptive names and comments leave hints to help the reader understand the intention behind the code. This lets us focus on the words instead of the syntax, only digging into the details of the code when we need to.

# Here's the same program but with better naming and documentation. Can you guess what it does now?

# wins = 2
# ties = 4

# # Football teams earn 3 points for a win and 1 for a tie.
# print(wins * 3 + ties)

# Starter style guide
# A style guide defines conventions for writing code in a clear and consistent way. Organizations use style guides to standardize how code looks, so it's seamless to jump from one person's code to another's.

# Coding conventions are only enforced by humans. Break a convention and your program still works. Break a rule and your program has an error. For example, it's a convention that variable names use lowercase letters, but it's a rule that variable names can't start with numbers.

# We've designed this starter style guide to help you write readable Python programs with expressions and variables. We'll add more conventions to our style guide as we go!

# Spacing and blank lines

# Use a single space before and after an operator. Do not use a space before or after a parenthesis, unless it's next to an operator.
# Use blank lines to separate groups of related lines of code. Organize code into logical sections, like paragraphs in an essay.

# Do

# height = 10
# area = (4 + 7) / 2 * height
# print("The area is " + str(area) + " sq cm.")

# # Don't

# height=10
# area = (4+7)/2  *  height
# print ( "The area is " + str (area) + " sq cm." )

# Line length
# Limit lines of code to a maximum of 79 characters. 
# Use extra parentheses and intermediate variables to break down complex lines of code, so it's obvious how to evaluate each expression.

# # Do

# vinegar_ml = (3 * 2) + 5
# coffee_ml = (2 / 3) * 8
# total_acid_ml = vinegar_ml + coffee_ml

# # Don't

# total_acid_ml = 3 * 2 + 5 + 2 / 3 * 8

# Comments

# Format comments as complete sentences, with a single space after the #. Start the comment with a capital letter and end it with punctuation.

# Use comments to explain the intention behind code (the why), not the mechanics of what the code is doing. Keep comments up-to-date with the latest code changes.

# Do

# temp = 12.5
# wind_chill = 4
# temp = temp - wind_chill

# # Convert the temperature to degrees Fahrenheit.
# temp = temp * (9 / 5) + 32

# # Don't

# temp = 12.5
# # wind chill
# x = 4
# #Subtract x from the temperature.
# temp = temp - x

# # Do the conversion.
# temp = temp * (9 / 5) + 32

# Variable names

# Use all lowercase letters and separate words with underscores, like last_login_time. This is called snake case.

# Use descriptive names. Names should describe the variable's purpose: what does this value represent? Avoid nonstandard abbreviations.

# Name variables using nouns, like width instead of how_wide. As an exception, name variables that contain boolean values like a yes or no question, like has_account.

# # Do

# title = "Python style guide"
# word_count = 671
# publish_year = 2024
# author = "Kim M"
# can_edit_doc = False

# # Don't

# style_guide = "Python style guide"
# x = 671
# publishYear = 2024
# written_by = "Kim M"
# edit_permission = False