import json

json_file_path = 'JSON\example_1.json'

with open(json_file_path,"r") as json_file:
    data = json.load(json_file)
    print(data,type(data))