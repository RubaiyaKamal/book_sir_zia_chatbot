import tkinter as tk
from tkinter import ttk
import pandas as pd
import os

class TodoListApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("To-Do List App")
        self.geometry("800x600")

        self.tasks_df = None
        self.tasks_file = "tasks.csv"

        self.load_tasks()

        self.create_widgets()

    def load_tasks(self):
        if os.path.exists(self.tasks_file):
            self.tasks_df = pd.read_csv(self.tasks_file)
        else:
            self.tasks_df = pd.DataFrame(columns=["Task", "Completed", "DueDate", "Priority"])
            self.tasks_df.to_csv(self.tasks_file, index=False)

    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Task list frame
        tasks_frame = ttk.LabelFrame(main_frame, text="Tasks", padding="10")
        tasks_frame.pack(fill=tk.BOTH, expand=True)

        self.task_list = ttk.Treeview(tasks_frame, columns=("Task", "DueDate", "Priority", "Completed"), show="headings")
        self.task_list.heading("Task", text="Task")
        self.task_list.heading("DueDate", text="Due Date")
        self.task_list.heading("Priority", text="Priority")
        self.task_list.heading("Completed", text="Completed")
        self.task_list.pack(fill=tk.BOTH, expand=True)

        # Input frame
        input_frame = ttk.LabelFrame(main_frame, text="Add/Edit Task", padding="10")
        input_frame.pack(fill=tk.X, pady=10)

        ttk.Label(input_frame, text="Task:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.task_entry = ttk.Entry(input_frame, width=40)
        self.task_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)

        ttk.Label(input_frame, text="Due Date:").grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
        self.duedate_entry = ttk.Entry(input_frame)
        self.duedate_entry.grid(row=0, column=3, padx=5, pady=5, sticky=tk.EW)

        ttk.Label(input_frame, text="Priority:").grid(row=0, column=4, padx=5, pady=5, sticky=tk.W)
        self.priority_combobox = ttk.Combobox(input_frame, values=["Low", "Medium", "High"])
        self.priority_combobox.grid(row=0, column=5, padx=5, pady=5, sticky=tk.EW)
        self.priority_combobox.set("Medium")

        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)

        ttk.Button(button_frame, text="Add Task", command=self.add_task).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Edit Task", command=self.edit_task).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Delete Task", command=self.delete_task).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Mark as Completed", command=self.toggle_complete).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear All Tasks", command=self.clear_all_tasks).pack(side=tk.RIGHT, padx=5)

        # Filter frame
        filter_frame = ttk.LabelFrame(main_frame, text="Filter Tasks", padding="10")
        filter_frame.pack(fill=tk.X, pady=10)

        ttk.Button(filter_frame, text="All", command=lambda: self.filter_tasks("All")).pack(side=tk.LEFT, padx=5)
        ttk.Button(filter_frame, text="Pending", command=lambda: self.filter_tasks("Pending")).pack(side=tk.LEFT, padx=5)
        ttk.Button(filter_frame, text="Completed", command=lambda: self.filter_tasks("Completed")).pack(side=tk.LEFT, padx=5)
        ttk.Button(filter_frame, text="High Priority", command=lambda: self.filter_tasks("High Priority")).pack(side=tk.LEFT, padx=5)

        # Status frame
        status_frame = ttk.LabelFrame(main_frame, text="Status", padding="10")
        status_frame.pack(fill=tk.X)

        self.total_tasks_label = ttk.Label(status_frame, text="Total Tasks: 0")
        self.total_tasks_label.pack(side=tk.LEFT, padx=10)
        self.completed_tasks_label = ttk.Label(status_frame, text="Completed Tasks: 0")
        self.completed_tasks_label.pack(side=tk.LEFT, padx=10)
        self.pending_tasks_label = ttk.Label(status_frame, text="Pending Tasks: 0")
        self.pending_tasks_label.pack(side=tk.LEFT, padx=10)

        self.task_list.bind("<<TreeviewSelect>>", self.on_task_select)

        self.refresh_task_list()

    def on_task_select(self, event):
        selected_item = self.task_list.focus()
        if selected_item:
            index = int(self.task_list.item(selected_item)["text"])
            task = self.tasks_df.loc[index]
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(0, task["Task"])
            self.duedate_entry.delete(0, tk.END)
            self.duedate_entry.insert(0, task["DueDate"])
            self.priority_combobox.set(task["Priority"])

    def refresh_task_list(self, tasks_to_display=None):
        for item in self.task_list.get_children():
            self.task_list.delete(item)

        tasks = self.tasks_df if tasks_to_display is None else tasks_to_display

        for index, row in tasks.iterrows():
            self.task_list.insert("", "end", text=str(index), values=(row["Task"], row["DueDate"], row["Priority"], row["Completed"]))
        
        self.update_status()

    def add_task(self):
        task = self.task_entry.get()
        due_date = self.duedate_entry.get()
        priority = self.priority_combobox.get()

        if task:
            new_task = pd.DataFrame([{"Task": task, "Completed": False, "DueDate": due_date, "Priority": priority}])
            self.tasks_df = pd.concat([self.tasks_df, new_task], ignore_index=True)
            self.save_tasks()
            self.refresh_task_list()
            self.task_entry.delete(0, tk.END)
            self.duedate_entry.delete(0, tk.END)

    def edit_task(self):
        selected_item = self.task_list.focus()
        if selected_item:
            index = int(self.task_list.item(selected_item)["text"])
            self.tasks_df.loc[index, "Task"] = self.task_entry.get()
            self.tasks_df.loc[index, "DueDate"] = self.duedate_entry.get()
            self.tasks_df.loc[index, "Priority"] = self.priority_combobox.get()
            self.save_tasks()
            self.refresh_task_list()

    def delete_task(self):
        selected_item = self.task_list.focus()
        if selected_item:
            index = int(self.task_list.item(selected_item)["text"])
            self.tasks_df = self.tasks_df.drop(index).reset_index(drop=True)
            self.save_tasks()
            self.refresh_task_list()

    def toggle_complete(self):
        selected_item = self.task_list.focus()
        if selected_item:
            index = int(self.task_list.item(selected_item)["text"])
            self.tasks_df.loc[index, "Completed"] = not self.tasks_df.loc[index, "Completed"]
            self.save_tasks()
            self.refresh_task_list()

    def update_status(self):
        total_tasks = len(self.tasks_df)
        completed_tasks = len(self.tasks_df[self.tasks_df["Completed"] == True])
        pending_tasks = total_tasks - completed_tasks

        self.total_tasks_label.config(text=f"Total Tasks: {total_tasks}")
        self.completed_tasks_label.config(text=f"Completed Tasks: {completed_tasks}")
        self.pending_tasks_label.config(text=f"Pending Tasks: {pending_tasks}")

    def save_tasks(self):
        self.tasks_df.to_csv(self.tasks_file, index=False)

    def clear_all_tasks(self):
        self.tasks_df = pd.DataFrame(columns=["Task", "Completed", "DueDate", "Priority"])
        self.save_tasks()
        self.refresh_task_list()

    def filter_tasks(self, filter_by):
        if filter_by == "All":
            self.refresh_task_list()
        elif filter_by == "Pending":
            filtered_df = self.tasks_df[self.tasks_df["Completed"] == False]
            self.refresh_task_list(tasks_to_display=filtered_df)
        elif filter_by == "Completed":
            filtered_df = self.tasks_df[self.tasks_df["Completed"] == True]
            self.refresh_task_list(tasks_to_display=filtered_df)
        elif filter_by == "High Priority":
            filtered_df = self.tasks_df[self.tasks_df["Priority"] == "High"]
            self.refresh_task_list(tasks_to_display=filtered_df)

if __name__ == "__main__":
    app = TodoListApp()
    app.mainloop()
