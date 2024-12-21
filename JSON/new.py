#import json

# data = {
#     "name":"John Roneth",
#     "age":30,
#     "city":"New York"
# }
# json_file_path = "JSON/test.json"

# with open(json_file_path,"w") as json_file:
#     json_data = json.dumps(data,indent=4)       #dumps is used to convert dictionary to json
#     json_file.write(json_data)
#     print("JSON data had been written to {json_file_path}")

#You are given a json file name students.json which contains information about students and their grades. Your task is to,
# 1.Read the json file
# 2.Display the names of all students who scored above 75
# 3.Add a new student record to the file
# 4.Save the updated data back to the json file
# [
#   {"name":"Alice","grade":85},
#   {"name":"Minura","grade":72},           This is an array of json object
#   {"name":"Omesh","grade":90}
# ] 

import json

with open("JSON/students.json","r") as json_file:
    data = json.load(json_file) 
    print(data)
for n in data:
    if (n["grade"]>75):
        print(n["name"])

add_data = {"name":"Sithira","grade":70}
data.append(add_data)
with open("JSON/students.json","w") as json_file:
    json_data = json.dumps(data,indent=4)
    json_file.write(json_data)
