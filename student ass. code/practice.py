import json
import os

FILE_NAME = "assignments.json"

# Load existing data
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Add new assignment
def add_task(tasks):
    print("\n--- Add New Assignment ---")
    title = input("Enter title: ")
    subject = input("Enter subject: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    priority = input("Enter priority (High/Medium/Low): ")

    task = {
        "title": title,
        "subject": subject,
        "deadline": deadline,
        "priority": priority,
        "status": "Pending"
    }

    tasks.append(task)
    save_tasks(tasks)
    print("✅ Assignment added successfully!\n")

# View all assignments
def view_tasks(tasks):
    print("\n--- Your Assignments ---")
    if not tasks:
        print("No assignments found.\n")
        return

    # Sort by deadline
    tasks.sort(key=lambda x: x["deadline"])

    for i, task in enumerate(tasks):
        print(f"\n{i+1}. {task['title']} ({task['subject']})")
        print(f"   Deadline: {task['deadline']}")
        print(f"   Priority: {task['priority']}")
        print(f"   Status: {task['status']}")

# Mark as completed
def mark_completed(tasks):
    view_tasks(tasks)
    choice = int(input("\nEnter assignment number to mark completed: ")) - 1

    if 0 <= choice < len(tasks):
        tasks[choice]["status"] = "Completed"
        save_tasks(tasks)
        print("✅ Marked as completed!\n")
    else:
        print("❌ Invalid choice\n")

# Delete assignment
def delete_task(tasks):
    view_tasks(tasks)
    choice = int(input("\nEnter assignment number to delete: ")) - 1

    if 0 <= choice < len(tasks):
        tasks.pop(choice)
        save_tasks(tasks)
        print("🗑️ Assignment deleted!\n")
    else:
        print("❌ Invalid choice\n")

# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("\n===== Assignment Tracker =====")
        print("1. Add Assignment")
        print("2. View Assignments")
        print("3. Mark as Completed")
        print("4. Delete Assignment")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye! Stay organized 😊")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()