def add_task(task_list, task):
    task_list.append(task)
    print(f"{task} added")

def remove_task(task_list, task):
    task_list.remove(task)
    print(f"{task} removed")