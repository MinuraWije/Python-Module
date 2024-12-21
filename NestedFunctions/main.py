# def outer(x):
#     def inner(y):
#         return x+y
#     return inner

# temp_value = outer(5)
# print(temp_value(7))

#Pass Function as argument
#Passing a function as an argument to another function in python

# def add(x,y):
#     return x+y
# def calculate(func,x,y):
#     return func(x,y)

# result = calculate(add,4,6)
# print(result)

# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         ordinary()
#     return inner

# def ordinary():
#     print("I am ordinary")

# get_decorated = make_pretty(ordinary)
# get_decorated()

# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner

# @make_pretty
# def ordinary():
#     print("I am ordinary")

# ordinary()

#Write a python program with the following requirements
#Create a decorator check_positive that,
#       1. Checks if the input to a function is a positive number
#       2. If the input is not positive print a message like "Input must be a positive number"
# Use this decorator on a function calculate_square_root()
#       1. Takes 1 number as input
#       2. Returns the square root of the input number

import math

def check_positive(func):
    def inner(x):
        if x>=0:
            func(x)
        else:
            return "Input must be a positive number"

@check_positive
def calculate_square_root(x):
    return math.sqrt(x)

calculate_square_root(9)