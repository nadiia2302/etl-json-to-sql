import json
import os

# try:
#    with open("task1_d.json","r") as file:
#     data = json.load(file)
# except json.JSONDecodeError as e:
#     print("Failed to load JSON", e)
#     exit()
# except FileNotFoundError as e:
#     print("file not found!",e)
# exit()

with open ('task1_d.json','r') as file:
    raw_data = file.read()
    replacements = {
        ":id=>": '"id":',
        ":title=>": '"title":',
        ":author=>": '"author":',
        ":genre=>": '"genre":',
        ":publisher=>": '"publisher":',
        ":year=>": '"year":',
        ":price=>": '"price":'
    }
    clean_data = raw_data
    for old, new in replacements.items():
        clean_data = clean_data.replace(old, new)
    correct_data = json.loads(clean_data)
    print(correct_data)


