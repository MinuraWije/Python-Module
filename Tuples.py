# sports = ("cricket","football","tennis")
# print(len(sports))            #To determine the number of items a tuple has
# print(type(sports))


#To make a tuple with 1 item we have to add a coma after the 1st item
# car = ("ferrari",)      #Without the coma this would be a string
# print(type(car))

# tuple_1 = ("dog","cat","10")
# tuple_1[1] = "rat"
# print(tuple_1)      #TypeError: 'tuple' object does not support item assignment

# my_tuple_1 = ("dog","cat","rabbit")     #Workaround for the above problem is to convert the tuple to a list and then change the value in the index and convert it back to a tuple
# my_tuple_2 = list(my_tuple_1)
# my_tuple_2[0] = "rat"
# my_tuple_1 = tuple(my_tuple_2)
# print(my_tuple_1,type(my_tuple_1))

# my_tuple_1 = (10,8,20,5)
# my_tuple_2 = (5,9,-1)

# my_list_1 = list(my_tuple_1)
# my_list_1.pop(2)
# my_list_2 = list(my_tuple_2)
# my_list_3 = my_list_1+my_list_2 
# my_list_3.sort()
# my_tuple_3 = tuple(my_list_3)
# print(my_tuple_3)

my_tuple_1 = ((1,10,8),("dog","cat","rat"),(True,False))
print(my_tuple_1[0][1], my_tuple_1[1][2], my_tuple_1[2][0])