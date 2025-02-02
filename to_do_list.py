import tkinter as tk
from tkinter import messagebox
import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        save_tasks(tasks)
        task_entry.delete(0, tk.END)
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        task_listbox.insert(tk.END, f"{index}. [{status}] {task['task']}")

def remove_task():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks.pop(selected_index)
        save_tasks(tasks)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def complete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks[selected_index]["completed"] = True
        save_tasks(tasks)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

def exit_app():
    root.destroy()

tasks = load_tasks()
root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=40)
task_entry.pack(side=tk.LEFT, padx=10)
add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

update_task_list()

button_frame = tk.Frame(root)
button_frame.pack()

remove_button = tk.Button(button_frame, text="Remove Task", command=remove_task)
remove_button.pack(side=tk.LEFT, padx=5)

complete_button = tk.Button(button_frame, text="Mark Completed", command=complete_task)
complete_button.pack(side=tk.LEFT, padx=5)

exit_button = tk.Button(button_frame, text="Exit", command=exit_app)
exit_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
