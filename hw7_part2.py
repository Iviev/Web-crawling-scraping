# 507/206 Homework 7 Part 2
import json

count = 0
#### Your Part 2 solution goes here ####
json_file = open("directory_dict.json", "r")
json_content = json_file.read()
loaded_directory_dict = json.loads(json_content) #loading it into a dictionary from a json string


for key in loaded_directory_dict.keys():
    if loaded_directory_dict[key]["title"] == "PhD student":
        count +=1


#### Your answer output (change the value in the variable, count)####
print('The number of PhD students: ', count)
