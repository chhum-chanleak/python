# print() function can take multiple parameters.

# print("Hello,", name)
# print(2, "Hello", True)

# 1. What is input()?
# Pauses the program
# Waits for the user to type something
# Returns what the user typed as a string (always a string)

# Example 1: Basic input (text)

# name = input("Enter your name: ")

# print("Hello,", name)

# What happens:

# Python shows: Enter your name:

# User types: Alice

# name becomes "Alice"

# Output: Hello, Alice

# Example 2: Input without a prompt

# user_input = input()
# print("You typed:", user_input)

# What happens:

# Program waits silently

# User types: hello

# Output: You typed: hello

# Example 3: Input + number problem (common beginner mistake)

# age = input("Enter your age: ")
# print(age + 5)

# ❌ This causes an error.

# Why?

# input() returns "20" (string)

# Python cannot add a number to a string

# Example 4: Converting input to a number (correct way)

# age = int(input("Enter your age: "))
# print(age + 5)

# What happens:

# User types: 20

# input() → "20"

# int("20") → 20

# Output: 25

# *Summary

# input() always returns a string

# Use int() or float() if you need numbers

# Prompt text is optional

# Nothing happens until the user presses Enter

# What will this print, and why?

# x = input("Enter something: ")
# print(type(x))