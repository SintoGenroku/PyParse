import json
import re

with open("films top250.json","r") as f:
    data = json.load(f)
for item in data:
   
    if item["genre"] == "фэнтези":
       print(item)

"""
 result = re.findall("США", item["country"])     потенциальные регулярки для упрощения поиска
    print(result)                                работает, но не так как хотелось
"""