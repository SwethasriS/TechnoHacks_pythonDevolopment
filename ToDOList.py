import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime, timedelta

class TodoListApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List")
        self.geometry("500x400")
        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        self.task_label = tk.Label(self, text="Add a Task:")
        self.task_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.task_entry = tk.Entry(self, width=30)
        self.task_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.time_label = tk.Label(self, text="Set Ending Time:")
        self.time_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.hour_var = tk.StringVar()
        self.minute_var = tk.StringVar()
        self.hour_var.set("00")
        self.minute_var.set("00")
        self.hour_menu = ttk.Combobox(self, width=3, textvariable=self.hour_var, values=[str(i).zfill(2) for i in range(24)])
        self.hour_menu.grid(row=1, column=1, padx=(0, 10), pady=5, sticky="w")
        self.minute_menu = ttk.Combobox(self, width=3, textvariable=self.minute_var, values=[str(i).zfill(2) for i in range(0, 60, 15)])
        self.minute_menu.grid(row=1, column=1, padx=(40, 10), pady=5, sticky="w")
        
        self.add_button = tk.Button(self, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=2, padx=10, pady=5)

        self.tree = ttk.Treeview(self, columns=("Task", "Ending Time"), show='headings')
        self.tree.heading("Task", text="Task")
        self.tree.heading("Ending Time", text="Ending Time")
        self.tree.column("Task", width=200)
        self.tree.column("Ending Time", width=100)
        self.tree.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        self.delete_button = tk.Button(self, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.update_button = tk.Button(self, text="Update Task", command=self.update_task)
        self.update_button.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.grid(row=3, column=2, padx=10, pady=5, sticky="e")

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def add_task(self):
        task = self.task_entry.get()
        hour = int(self.hour_var.get())
        minute = int(self.minute_var.get())
        if task:
            ending_time = datetime.now() + timedelta(hours=hour, minutes=minute)
            self.tasks.append((task, ending_time))
            self.tree.insert("", tk.END, values=(task, ending_time.strftime('%H:%M')))
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a task.")

    def delete_task(self):
        selected_item = self.tree.selection()
        if selected_item:
            for item in selected_item:
                self.tree.delete(item)
                index = self.tree.index(item)
                del self.tasks[index]
        else:
            messagebox.showerror("Error", "Please select a task to delete.")

    def update_task(self):
        selected_item = self.tree.selection()
        if selected_item:
            task = self.task_entry.get()
            hour = int(self.hour_var.get())
            minute = int(self.minute_var.get())
            if task:
                ending_time = datetime.now() + timedelta(hours=hour, minutes=minute)
                for item in selected_item:
                    index = self.tree.index(item)
                    self.tasks[index] = (task, ending_time)
                    self.tree.item(item, values=(task, ending_time.strftime('%H:%M')))
                    self.task_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Please enter a task.")
        else:
            messagebox.showerror("Error", "Please select a task to update.")

if __name__ == "__main__":
    app = TodoListApp()
    app.mainloop()
