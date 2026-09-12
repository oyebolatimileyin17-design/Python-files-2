#School class dictionary
import json 

data = {"name": "Nathan", "class": "JSS1", "score": 90}
json_string = json.dumps(data)
print(json_string)

print(type(json_string))