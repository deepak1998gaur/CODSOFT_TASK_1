import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        # Task entry
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Add Task button
        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=1, padx=5, pady=10)

        # Task list
        self.task_listbox = tk.Listbox(root, height=12, width=60)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Remove Task button
        remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        remove_button.grid(row=2, column=0, padx=5, pady=10)

        # Clear All button
        clear_button = tk.Button(root, text="Clear All", command=self.clear_all_tasks)
        clear_button.grid(row=2, column=1, padx=5, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = int(selected_task_index[0])
            del self.tasks[selected_task_index]
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def clear_all_tasks(self):
        self.tasks = []
        self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
