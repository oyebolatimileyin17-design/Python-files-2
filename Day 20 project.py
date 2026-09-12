import todo_logic

my_list = []
todo_logic.add_task(my_list, "Wake up")
todo_logic.add_task(my_list, "Exercise")
print(my_list)

todo_logic.remove_task(my_list, "Exercise")
print(my_list)
