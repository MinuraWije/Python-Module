#DEFUALT ARGUMENTS

# def calculate(a,b=5):
#     print(a+b)
# calculate(6,8)      #14
# calculate(6)        #11

# def numbers(a,b=5,c):       #This is wrong
#     return a+b+c

# def numbers(a,c,b=5):       #This is correct because all default values should be given to the right side of the given parameters
#     return a+b+c


#POSITIONAL ARGUMENTS

# def numbers(a,b):             #Sent in orders
#     return a+b
# numbers(5,6)


#KEYWORD ARGUMENTS
# def numbers(a,b):             #Order does not matter anymore as the specific arguments are given here
#     return a+b
# numbers(a=5,b=8)

# define a function name calculate_total_cost with the following parameters
# item_price:mandatory
# quantity:mandatory
# discount:optional, default=0   A percentage applied to the total price
# tax:optional, default=0        A percentage applied for the discounted price


# def calculate_total_cost(item_price,quantity,discount=0,tax=0):
#     price = item_price*quantity
#     discounted_price = price-(price*discount/100)
#     print(discounted_price-(discounted_price*tax/100))

# calculate_total_cost(50,10,10,20)


#ARBITRARY POSITIONAL ARGUMENTS

# def arbitrary_positional_arguments(*args):          #Can send any number of arguments as needed.(Does the same thing as var args used in java)
#     print(args,type(args))                          #Type is tuple
# arbitrary_positional_arguments("car",True,3)

#Write a function to calculate the sum of any given numbers

# def num_total(*nums):
#     total=0
#     for num in nums:
#         total+=num
#     print(total)
# num_total(1,6,10,89)

#Write a python function called summarise_grades that accept a student's name as a mandatory argument and an arbitrary number of grade scores. 
# The function should,
#   1.Print the student's name
#   2.Calculate and print the highest grade,lowest grade and the average grade from the provided discourse
#If no grades are provided you should print "no grades available"

# def summarize_grades(name,*grades):
#     print("Student name :", name)
#     if not name :
#         print("Name is mandatory")
#     if not grades:
#         print("No grades available")
#     else:
#         print("The highest grade is",max(grades))
#         print("The lowest grade is",min(grades))
#         print("The total grade is",sum(grades))
#         print("The average grade is",sum(grades)/len(grades))

# summarize_grades("Minura",20,55,80,11)
# summarize_grades("Sithira")


#ARBITRARY KEYWORD ARGUMENTS(type is dictionary)

# def arb_key_arguments(**kwargs):
#     print(kwargs,type(kwargs))
#     for key, value in kwargs.items():
#         print("Key=",key,"   Value",value)
# arb_key_arguments(name="Minura",age=21,city="Moratuwa")

#EMPLOYEE MANAGEMENT SYSTEM
#Write a python function employee_info that accepts a required name parameter and an arbitrary number of keyword arguments representing additional 
# details about the employee. The function should,
#   1.Print the employee's name iterate through the keyword arguments and print each key value pair in the format "<key>:<value>" 
#   2.Return a dictionary with all the employee details

def employee_info(name,**details):
    print("Name of the employee is :",name)
    if not name:
        print("Name is mandatory")
    else :
        for key,value in details.items():
            print(key,":",value)
        print({"name":name}|details)            #Dict merging

employee_info(name="Minura",age=21,city="Moratuwa")