import json

todo_list = ["Wake up and pray", "Exercise", "Read a chapter"]

with open("todo.json", "w") as file:
      json.dump(todo_list, file)

with open("todo.json", "r") as file:
      loaded_list = json.load(file)
print(loaded_list)