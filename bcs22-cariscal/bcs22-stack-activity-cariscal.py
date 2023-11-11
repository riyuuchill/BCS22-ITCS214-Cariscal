class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        self.tasks.append(Task(title, description))

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. Title: {task.title}, Description: {task.description}, Completed: {task.completed}")

    def run(self):
        while True:
            print("\n1. Add a task\n2. Mark a task as completed\n3. Display tasks\n4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                self.add_task(title, description)

            elif choice == "2":
                index = int(input("Enter the index of the task to mark as completed: ")) - 1
                self.mark_completed(index)

            elif choice == "3":
                self.display_tasks()

            elif choice == "4":
                print("Exiting the task manager. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    manager = TaskManager()
    manager.run()
