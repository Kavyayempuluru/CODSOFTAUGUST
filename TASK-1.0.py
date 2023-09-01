
import tkinter as tk

class ToDoList:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")

        self.tasks = []

        self.task_label = tk.Label(master, text="Task:")
        self.task_label.pack()

        self.task_entry = tk.Entry(master)
        self.task_entry.pack()

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.listbox = tk.Listbox(master)
        self.listbox.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            task = self.tasks.pop(task_index)
            self.listbox.delete(task_index)
            print(f"Deleted task: {task}")
        except IndexError:
            pass

root = tk.Tk()

root.geometry('300x400')
root.resizable(0, 0)
root.config(bg="PaleVioletRed")

my_todo_list = ToDoList(root)
root.mainloop()
