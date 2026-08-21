import os
import json

SAVE_FILE = "todolist/save.json"

def save_list(data):
    os.makedirs(os.path.dirname(SAVE_FILE), exist_ok=True)
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=2)

def load_list():
    if not os.path.exists(SAVE_FILE):
        return []
    try:
        with open(SAVE_FILE) as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def remove_item():
    pass

def add_item():
    data = load_list()

    task = input("Task: ")
    done_input = input("Done? (y/n): ").strip().lower()
    done = done_input == "y"

    item = {
        "id": len(data) + 1,
        "task": task,
        "done": done,
    }

    data.append(item)
    save_list(data)
    return data

def view_list():
    data = load_list()
    if not data:
        print("No tasks yet.")
        return

    for item in data:
        status = "x" if item["done"] else " "
        print(f"[{status}] {item['id']}. {item['task']}")