import json

class Task:
    def __init__(self, name, done=False):
        self.name = name
        self.done = done

tasks = []   # ← renamed from "task" to "tasks"

def add_task(name):
    tasks.append(Task(name))
    print(f"Task {name} added.")

def complete_task(name):
    for task in tasks:          # ← now looping over "tasks", naming the loop var "task"
        if task.name == name:
            task.done = True
            print(f"Task {name} completed.")

def list_tasks():
    for task in tasks:          # ← same fix here
        status = "✓" if task.done else "✗"
        print(f"[{status}] {task.name}")

def save_tasks():
    with open("tasks.json", "w") as file:
        data = [{"name": t.name, "done": t.done} for t in tasks]
        json.dump(data, file)

def load_tasks():
    global tasks
    with open("tasks.json", "r") as file:
        data = json.load(file)
        tasks = [Task(item["name"], item["done"]) for item in data]
add_task("Wake up")
add_task("Exercise")
list_tasks()

complete_task("Wake up")
list_tasks()

save_tasks()

tasks = []          # simulate starting fresh
load_tasks()
list_tasks()  