# response_code = 201

# match response_code:
#     case 200:
#         print("OK")
#     case 201:
#         print("Created")
#     case 404:
#         print("404 not found.")
#     case 500:
#         print("Internal server error.")
#     case _:             # defualt response 
#         print("Something else")    

# x = int(input("Enter number : "))

# match x:
#     case 0:
#         print("Zero")
#     case -1:
#         print("Negative one")
#     case 1:
#         print("Positive one")
#     case x if x>1:
#         print("Positive number greater than one")
#     case _ if x<1:
#         print("Negative number less than negative one")
#     case _:
#         print("Unmatched case")

# numbers = [4,3,7]

# match numbers:
#     case [x,y]:
#         print(x*y)
#     case [x,y,z]:
#         print(x+y+z)
#     case _:
#         print("The list does not contain 2 or 3 numbers.")

x = [2,]    

match x:
    case []:
        print("Empty list")
    case [a,]:
        print("List has one element")
    case [a,b]:
        print("List has two element")
    case _:
        print("This is something else") 