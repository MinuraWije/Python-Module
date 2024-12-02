# dict_1 = {
#     "name":"sugar",
#     "weight":"1kg",
#     "price": 130.50
# }
# print(dict_1)

# dict_1 = {                  #No errors are shown when duplicate keys are given
#     "name":"sugar",         #But length of dictionary does not count duplicates.
#     "weight":"1kg",
#     "weight":"2kg",
#     "price": 130.50
# }
# print(dict_1,len(dict_1))
# print(dict_1["weight"])     #The value of a key can be taken by writing the key name

# dict_1 = {
#     "name":"Minura",
#     "age":30,
#     "is_Student":True,
#     "grades":[93,86,98],
#     "coordinates":(12.345,56.805),
#     "preferences":{"color":"blue","food":"pizza"}
# }
# print(dict_1)

# dict_1 = {                  
#     "name":"sugar",         
#     "weight":"1kg",
#     "price": 130.50
# }
# dict_1["price"] = 350.00
# print(dict_1)

# dict_1 = {                  
#     "name":"sugar",         
#     "weight":"1kg",
#     "price": 130.50
# }
# dict_1.update({"weight":"2kg","price":220.50})
# print(dict_1)

# dict_1 = {                  #Adding an item   
#     "name":"sugar",         
#     "weight":"1kg",
#     "price": 130.50
# }
# dict_1["color"] = "white"
# print(dict_1,len(dict_1))

# dict_1 = {                  #Removing an item   
#     "name":"sugar",         
#     "weight":"1kg",
#     "price": 130.50
# }
# dict_1.pop("weight")
# print(dict_1)

# dict_1 = {                  #Removing the last item of the dictionary  
#     "name":"sugar",         
#     "weight":"1kg",
#     "price": 130.50
# }
# dict_1.popitem()
# print(dict_1)

# dict_1 = {                  #Deleting an item   
#     "name":"sugar",         
#     "weight":"1kg",
#     "price": 130.50
# }
# del dict_1["weight"]
# print(dict_1)
# dict_1.clear()      #To delete the data within the dictionary
# print(dict_1)
# del dict_1          #To delete the dictionary itself 
# print(dict_1)

# dict_1 = {                  
#     "name":"sugar",         
#     "weight":"1kg",
#     "price": 130.50
# }
# dict_2 = dict_1.copy()
# dict_1.update({"weight":"5kg"})
# print(dict_1,dict_2)

# dict_1 = {                      #To get all keys in a dictionary                  
#     "name":"sugar",         
#     "weight":"1kg",
#     "price": 130.50
# }
# print(dict_1.keys())

my_dict = {
    'a':1,
    'b':2,
    'c':3
}
my_dict['b']
print(my_dict.get('b',0))
print(my_dict.get('d'))