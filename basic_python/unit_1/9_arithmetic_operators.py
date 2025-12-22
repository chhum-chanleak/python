# 1. Arithmetic expressions
# A basic arithmetic expression consists of a value, an operator, and a value, where each value is an integer or a float. In Python, the standard arithmetic operators are +, -, *, **, /, //, and %.

# operator	            operation	          example	read as
# +	addition	           x + y	              x plus y
# -	subtraction	         x - y	              x minus y
# *	multiplication	     x * y	              x times y
# **	exponentiation	   x ** y	              x to the power of y
# /	float division	     x / y	              x divided by y
# //	floor division	   x // y	              x floor divided by y
# %	modulus (remainder)	 x % y	              x modulo y

# Why is this useful?

# Floor division tells us the number of times that one number can be evenly divided into another. For example, if I want to calculate how many complete pairs of socks I have, I can use the expression num_socks // 2 to ignore any unpaired socks.

# Modulus tells us if one number is a multiple of another. For example, we can use the modulo operator to check if a number is even or odd. An even number divided by 2 has no remainder, so num % 2 should evaluate to 0.

# Example

# Try: x = 47, y = 100 | x = 10.6, y = 2 | x = -5.0, y = -2.0

x = 47
y = 100

print("x plus y evaluates to...")
print(x + y)

print("x minus y evaluates to...")
print(x - y)

print("x times y evaluates to...")
print(x * y)

print("x to the power of y evaluates to...")
print(x ** y)

print("x divided by y evaluates to...")
print(x / y)

print("x floor divided by y evaluates to...")
print(x // y)

print("x modulo y evaluates to...")
print(x % y)

# What about strings?

# Aside from the + operator, arithmetic operators don't apply to strings. As a human, I can't divide a word by another word, so neither can the computer. What's "potato" divided by "tomato"?
# If you try to use the -, *, **, /, //, or % operator on a string value, you'll get a runtime error that looks like:
# TypeError: unsupported operand type(s) for /: 'str' and 'str'
# The only exception is that you can multiply a string by an integer. The expression "ha" * 3 evaluates to the string "hahaha"! The computer just repeats the string that number of times.