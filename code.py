class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"Task {index}:")
                print(f"Title: {task.title}")
                print(f"Description: {task.description}")
                print(f"Due Date: {task.due_date}")
                print()

# Create a TaskManager instance
task_manager = TaskManager()

# Create some tasks
task1 = Task("Complete project", "Finish the task manager project", "2023-06-30")
task2 = Task("Study for exam", "Review chapters 1-5 for the upcoming exam", "2023-07-05")

# Add tasks to the manager
task_manager.add_task(task1)
task_manager.add_task(task2)

# Display tasks
task_manager.display_tasks()

# Remove a task
task_manager.remove_task(task1)

# Display tasks after removal
task_manager.display_tasks()

