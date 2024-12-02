#INVOKING MODULES AND THEIR FUNCTIONS

#1ST WAY

# import my_calculator.addition
# import my_calculator.subtraction

# result1 = my_calculator.addition.add(5,3)
# result2 = my_calculator.subtraction.subtract(10,4)

# print("Addition result :",result1)
# print("Subtraction result :",result2)

#2ND WAY

# from my_calculator import addition
# from my_calculator import subtraction

# result1 = addition.add(5,3)
# result2 = subtraction.subtract(10,4)

# print("Addition result :",result1)
# print("Subtraction result :",result2)

#3RD WAY


# from my_calculator.addition import add
# from my_calculator.subtraction import subtract

# result1 = add(5,3)
# result2 = subtract(10,4)

# print("Addition result :",result1)
# print("Subtraction result :",result2)


from my_calculator import add,subtract

result1 = add(5,3)
result2 = subtract(10,4)

print("Addition result :",result1)
print("Subtraction result :",result2)



