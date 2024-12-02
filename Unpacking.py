# my_list = [10,12,8]
# x,y,z = my_list
# print(x,y,z)
# my_tuple = (20,6,19)
# a,b,c = my_tuple
# print(a,b,c)

person = {
    "name":"Minura",
    "age":21,
    "gender": "Male"
}
for key,value in person.items():
    print(key, value)
for key in person.keys():
    print(key)
for value in person.values():
    print(value)