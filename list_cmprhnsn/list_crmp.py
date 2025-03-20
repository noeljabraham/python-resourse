# list comprehension
from function.exersice_1 import add_two_numbers

# syntax
# [i for i in iterable if expression]

# For instance if you want to change a string to a list of characters.
# language = 'Python'
# lst= [i for i in language]
# print(lst)

# For instance if you want to generate a list of numbers
# numbers= [i for i in range(11)]
# print(numbers)

# List comprehension can be combined with if expression
# even=[i for i in range(21) if i%2==0]
# print(even)

# Lambda Function

# # syntax
# x = lambda param1, param2, param3: param1 + param2 + param2
# print(x(arg1, arg2, arg3))

# add_two_numbers: lambda  a, b : a+b
# print(add_two_numbers(2,3))

print((lambda a,b: a+b )(2,3))
