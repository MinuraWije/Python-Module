# add = lambda x,y: x+y
# print(add(3,5))

# print((lambda x,y: x+y)(5,3))

#Write a python program that,
#   1.Takes a list of tuples,where each tuple contains a name and age.
#   2.Use a lambda function to filter out the tuples where the age is less than 18
#   3.Print the list of tuples after filering 

# people = [("Minura",21),("John",17),("Andrew",21),("Kate",15)]

# check = lambda details: details[1]>=18
# print(list(filter(check,people)))

# def myfunc(h):
#     return lambda a : a*h

# mydoubler = myfunc(2)
# print(mydoubler(5))
# mytripler = myfunc(3)
# print(mytripler(15))

#Write a lambda function to return the max value between 2 numbers given

# print((lambda num1, num2: num1 if(num1>num2) else num2) (20,36)) 


