import os
import pandas as pd
from datetime import datetime

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def display_tasks(df):
    clear_screen()
    if df.empty:
        print("No tasks found.")
    else:
        print(df.to_string(index=False))

    total_tasks = len(df)
    completed_tasks = len(df[df["status"] == "Completed"])
    pending_tasks = total_tasks - completed_tasks

    print("\n--- Task Counts ---")
    print(f"Total: {total_tasks}")
    print(f"Completed: {completed_tasks}")
    print(f"Pending: {pending_tasks}")

def add_task(file_path):
    title = input("Enter task title: ")
    due_date_str = input("Enter due date (YYYY-MM-DD, optional): ")
    priority = input("Enter priority (High, Medium, Low, optional): ")

    due_date = ( 
        datetime.strptime(due_date_str, "%Y-%m-%d").date()
        if due_date_str
        else None
    )

    new_task = {
        "title": title,
        "status": "Pending",
        "due_date": due_date,
        "priority": priority,
    }

    df = pd.read_csv(file_path)
    df = pd.concat([df, pd.DataFrame([new_task])], ignore_index=True)
    df.to_csv(file_path, index=False)
    print("Task added successfully!")

def edit_task(file_path):
    df = pd.read_csv(file_path)
    display_tasks(df)

    try:
        task_index = int(input("Enter the index of the task to edit: "))
        if 0 <= task_index < len(df):
            new_title = input("Enter the new title: ")
            df.loc[task_index, "title"] = new_title
            df.to_csv(file_path, index=False)
            print("Task edited successfully!")
        else:
            print("Invalid task index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(file_path):
    df = pd.read_csv(file_path)
    display_tasks(df)

    try:
        task_index = int(input("Enter the index of the task to delete: "))
        if 0 <= task_index < len(df):
            df = df.drop(index=task_index).reset_index(drop=True)
            df.to_csv(file_path, index=False)
            print("Task deleted successfully!")
        else:
            print("Invalid task index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def mark_task_completed(file_path):
    df = pd.read_csv(file_path)
    display_tasks(df)

    try:
        task_index = int(input("Enter the index of the task to mark as completed: "))
        if 0 <= task_index < len(df):
            df.loc[task_index, "status"] = "Completed"
            df.to_csv(file_path, index=False)
            print("Task marked as completed!")
        else:
            print("Invalid task index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def filter_tasks(df):
    print("\nFilter by:")
    print("1. All")
    print("2. Completed")
    print("3. Pending")
    print("4. High Priority")

    filter_choice = input("Enter your choice: ")

    if filter_choice == "1":
        display_tasks(df)
    elif filter_choice == "2":
        completed_tasks = df[df["status"] == "Completed"]
        display_tasks(completed_tasks)
    elif filter_choice == "3":
        pending_tasks = df[df["status"] == "Pending"]
        display_tasks(pending_tasks)
    elif filter_choice == "4":
        high_priority_tasks = df[df["priority"] == "High"]
        display_tasks(high_priority_tasks)
    else:
        print("Invalid choice.")

def clear_all_tasks(file_path):
    confirmation = input("Are you sure you want to clear all tasks? (y/n): ")
    if confirmation.lower() == "y":
        df = pd.DataFrame(
            columns=["title", "status", "due_date", "priority"]
        )
        df.to_csv(file_path, index=False)
        print("All tasks cleared.")
    else:
        print("Operation canceled.")
