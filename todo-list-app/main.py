
import os
import pandas as pd
from datetime import datetime
from utils import (
    clear_screen,
    display_tasks,
    add_task,
    edit_task,
    delete_task,
    mark_task_completed,
    filter_tasks,
    clear_all_tasks,
)

DATA_FILE = "data/tasks.csv"

def main():
    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(
            columns=["title", "status", "due_date", "priority"]
        )
        df.to_csv(DATA_FILE, index=False)

    while True:
        clear_screen()
        df = pd.read_csv(DATA_FILE)
        display_tasks(df)

        print("\nOptions:")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Filter Tasks")
        print("6. Clear All Tasks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(DATA_FILE)
        elif choice == "2":
            edit_task(DATA_FILE)
        elif choice == "3":
            delete_task(DATA_FILE)
        elif choice == "4":
            mark_task_completed(DATA_FILE)
        elif choice == "5":
            filter_tasks(df)
        elif choice == "6":
            clear_all_tasks(DATA_FILE)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
