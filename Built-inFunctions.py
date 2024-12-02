#abs()       Returns the absolute value

# print(abs(-20))
# print(abs(20))

#map()      Used to apply a given function to every item in an iterable(such as list,tuple,or other sequence) and 
# return an iterator that contains the result. It is considered as map type. Can have more than 1 iterable be checked with 1 map.

# def find_square(x):
#     return x*x

# my_list=[4,8,10]
# result = map(find_square,my_list)
# print(result,type(result))
# result = list(result)
# print(result,type(result))

# my_list_1 = [10,12,7,5]
# my_list_2 = [9,5,4,1]

# def find_sum(num1,num2):
#     return num1+num2


# result = list(map(find_sum,my_list_1,my_list_2))
# print(result,type(result))

#You have a list of integers representing temperatures in celcius
# Temperatures = [20,30,25,40,50]
# Write a python program using the map function to convert these temperatures into fahrenheits. Use the formula Fahrenheit = celcius*9/5+32

# temperatures = [20,30,25,40,50]

# def converter(celc):
#     return celc*9/5+32

# result = list(map(converter,temperatures))
# print(result)


#filter()     #Filter elements from an iterable based on a specified condition. It creates a new iterable containing only elements that satisfy the given condition.
# Filter can only take in 1 iterable and gives either true or false based on the given condition.

#You are given my_list = [5,7,8,3,12,14] use the filter function to filter out odd numbers.

my_list = [5,7,8,3,12,14]
def even(num):
    return num%2==0
print(filter(even,my_list))
print(list(filter(even,my_list)))