
import csv
import os
import datetime
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# CSV file path
CSV_FILE = 'tasks.csv'
FIELDNAMES = ['id', 'task', 'status', 'priority', 'due_date']

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_all_tasks():
    """Reads all tasks from the CSV file."""
    if not os.path.exists(CSV_FILE):
        return []
    with open(CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def add_task():
    """Adds a new task to the CSV file."""
    print(Fore.GREEN + "\n➕ Add a New Task")
    print("-----------------")
    task = input("Enter the task description: ")
    
    while True:
        priority = input("Enter priority (Low, Medium, High): ").capitalize()
        if priority in ['Low', 'Medium', 'High']:
            break
        else:
            print(Fore.RED + "Invalid priority. Please choose from Low, Medium, or High.")

    while True:
        due_date = input("Enter due date (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(due_date, '%Y-%m-%d')
            break
        except ValueError:
            print(Fore.RED + "Invalid date format. Please use YYYY-MM-DD.")

    tasks = get_all_tasks()
    new_id = len(tasks) + 1
    
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        if not os.path.exists(CSV_FILE) or os.path.getsize(CSV_FILE) == 0:
            writer.writeheader()
        writer.writerow({'id': new_id, 'task': task, 'status': 'Pending', 'priority': priority, 'due_date': due_date})
    
    print(Fore.GREEN + "\nTask added successfully!")
    input("Press Enter to continue...")

def display_tasks(tasks):
    """Displays the list of tasks."""
    print("\n📝 Task List")
    print("-----------")
    if not tasks:
        print(Fore.YELLOW + "No tasks found.")
        return

    print(f"{'ID':<5} {'Task':<30} {'Status':<15} {'Priority':<15} {'Due Date':<15}")
    print("-" * 80)

    for task in tasks:
        status_color = Fore.GREEN if task['status'] == 'Completed' else Fore.YELLOW
        priority_color = {
            'High': Fore.RED,
            'Medium': Fore.YELLOW,
            'Low': Fore.GREEN
        }.get(task['priority'], Fore.WHITE)

        print(f"{task['id']:<5} {task['task']:<30} {status_color}{task['status']:<15}{Style.RESET_ALL} {priority_color}{task['priority']:<15}{Style.RESET_ALL} {task['due_date']:<15}")

def mark_task_completed():
    """Marks a task as completed."""
    print(Fore.GREEN + "\n✅ Mark a Task as Completed")
    print("---------------------------")
    tasks = get_all_tasks()
    display_tasks(tasks)

    if not tasks:
        return

    while True:
        try:
            task_id = int(input("Enter the ID of the task to mark as completed: "))
            if 1 <= task_id <= len(tasks):
                break
            else:
                print(Fore.RED + "Invalid task ID.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")

    tasks[task_id - 1]['status'] = 'Completed'

    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(tasks)

    print(Fore.GREEN + "\nTask marked as completed!")
    input("Press Enter to continue...")

def delete_task():
    """Deletes a task."""
    print(Fore.RED + "\n❌ Delete a Task")
    print("-----------------")
    tasks = get_all_tasks()
    display_tasks(tasks)

    if not tasks:
        return

    while True:
        try:
            task_id = int(input("Enter the ID of the task to delete: "))
            if 1 <= task_id <= len(tasks):
                break
            else:
                print(Fore.RED + "Invalid task ID.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")

    deleted_task = tasks.pop(task_id - 1)

    # Re-assign IDs
    for i, task in enumerate(tasks):
        task['id'] = i + 1

    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(tasks)

    print(Fore.GREEN + f"\nTask '{deleted_task['task']}' deleted successfully!")
    input("Press Enter to continue...")

def edit_task():
    """Edits a task."""
    print(Fore.YELLOW + "\n✏️ Edit a Task")
    print("--------------")
    tasks = get_all_tasks()
    display_tasks(tasks)

    if not tasks:
        return

    while True:
        try:
            task_id = int(input("Enter the ID of the task to edit: "))
            if 1 <= task_id <= len(tasks):
                break
            else:
                print(Fore.RED + "Invalid task ID.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")

    task_to_edit = tasks[task_id - 1]

    print("\nEnter the new details (leave blank to keep current value):")
    new_task = input(f"New description ({task_to_edit['task']}): ") or task_to_edit['task']
    
    while True:
        new_priority = input(f"New priority ({task_to_edit['priority']}): ").capitalize() or task_to_edit['priority']
        if new_priority in ['Low', 'Medium', 'High']:
            break
        else:
            print(Fore.RED + "Invalid priority. Please choose from Low, Medium, or High.")

    while True:
        new_due_date = input(f"New due date ({task_to_edit['due_date']}): ") or task_to_edit['due_date']
        try:
            datetime.datetime.strptime(new_due_date, '%Y-%m-%d')
            break
        except ValueError:
            print(Fore.RED + "Invalid date format. Please use YYYY-MM-DD.")

    tasks[task_id - 1] = {
        'id': task_id,
        'task': new_task,
        'status': task_to_edit['status'],
        'priority': new_priority,
        'due_date': new_due_date
    }

    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(tasks)

    print(Fore.GREEN + "\nTask updated successfully!")
    input("Press Enter to continue...")

def filter_tasks():
    """Filters and displays tasks based on user's choice."""
    print(Fore.CYAN + "\n🔍 Filter Tasks")
    print("----------------")
    print("1. All tasks")
    print("2. Completed tasks")
    print("3. Pending tasks")
    print("4. High Priority tasks")

    choice = input("Enter your choice (1-4): ")
    tasks = get_all_tasks()

    if choice == '1':
        filtered_tasks = tasks
    elif choice == '2':
        filtered_tasks = [task for task in tasks if task['status'] == 'Completed']
    elif choice == '3':
        filtered_tasks = [task for task in tasks if task['status'] == 'Pending']
    elif choice == '4':
        filtered_tasks = [task for task in tasks if task['priority'] == 'High']
    else:
        print(Fore.RED + "Invalid choice.")
        input("Press Enter to continue...")
        return

    display_tasks(filtered_tasks)
    input("\nPress Enter to continue...")

def clear_all_tasks():
    """Deletes all tasks after confirmation."""
    print(Fore.RED + "\n🧹 Clear All Tasks")
    print("-------------------")
    confirm = input("Are you sure you want to delete all tasks? (y/n): ").lower()
    if confirm == 'y':
        if os.path.exists(CSV_FILE):
            os.remove(CSV_FILE)
        print(Fore.GREEN + "\nAll tasks have been deleted.")
    else:
        print(Fore.YELLOW + "\nOperation cancelled.")
    input("Press Enter to continue...")

def download_tasks():
    """Downloads all tasks to a new CSV file."""
    print(Fore.CYAN + "\n📥 Download Tasks to CSV")
    print("-------------------------")
    tasks = get_all_tasks()
    if not tasks:
        print(Fore.YELLOW + "No tasks to download.")
        input("Press Enter to continue...")
        return

    filename = input("Enter the filename for the backup CSV (e.g., tasks_backup.csv): ")
    if not filename.endswith('.csv'):
        filename += '.csv'

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(tasks)

    print(Fore.GREEN + f"\nTasks successfully downloaded to {filename}")
    input("Press Enter to continue...")

def main():
    """Main function to run the to-do list application."""
    while True:
        clear_screen()
        print(Fore.YELLOW + Style.BRIGHT + "🚀 To-Do List Application 🚀")
        print("==============================")
        
        tasks = get_all_tasks()
        display_tasks(tasks)
        
        print("\n" + Fore.CYAN + "What would you like to do?")
        print("1. ➕ Add a new task")
        print("2. ✏️ Edit a task")
        print("3. ❌ Delete a task")
        print("4. ✅ Mark a task as completed")
        print("5. 🔍 Filter tasks")
        print("6. 🧹 Clear all tasks")
        print("7. 📥 Download tasks to CSV")
        print("8. 🚪 Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            edit_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            mark_task_completed()
        elif choice == '5':
            filter_tasks()
        elif choice == '6':
            clear_all_tasks()
        elif choice == '7':
            download_tasks()
        elif choice == '8':
            print(Fore.GREEN + "Goodbye! 👋")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == '__main__':
    main()
