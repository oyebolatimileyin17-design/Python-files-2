todo_list = ["Wake up n pray", "Exercise", "Read a chapter"]

with open("todo.txt", "w") as file:
     for item in todo_list:
          file.write(item + "\n")

with open("todo.txt", "r") as file:
     print(file.read())
