from abc import ABC, abstractmethod
import json
import csv

class Task:
    def __init__(self, task_id, title, task_desc, due_date, status):
        self.task_id = task_id
        self.title = title
        self.task_desc = task_desc
        self.due_date = due_date
        self.status = status
   
    def to_dict(self):
        return {
             "Task ID" : self.task_id,
             "Title" : self.title,
             "Description" : self.task_desc,
             "Due Date" : self.due_date,
             "Status" : self.status
             }
    
    @staticmethod
    def from_dict(data):
        return Task(data["Task ID"], data["Title"], data["Description", data.get("Due Date"), data["Status"]])

class FileStoring(ABC):
    @abstractmethod
    def save(self, tasks):
        pass

    @abstractmethod
    def load(self,tasks):
        pass

class CSVFileStoring(FileStoring):
    def __init__(self, filename = "tasks.csv"):
        self.filename = filename

    def save(self, tasks):
        with open(self.filename, 'w', newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Task ID", "Title", "Description", "Due Date", "Status"])
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())

    def load(self):
        tasks = []
        try:
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    tasks.append(Task.from_dict(row))
        except FileNotFoundError:
            pass
        return tasks

class JSONFileStoring(FileStoring):
    def __init__(self, filename = 'tasks.json'):
        self.filename = filename

    def save(self, tasks):
        with open(self.filename, 'w') as file:
            json.dump([task.to_dict() for task in tasks], file, indent=2)
    
    def load(self):
        tasks = []
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                tasks = [Task.from_dict(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            pass
        return tasks
    
class ToDoProg:
    def __init__(self, file_storing: FileStoring):
        self.file_storing = file_storing
        self.tasks = file_storing.load()

    def add_task(self, task):
        self.tasks.append(task)
        print("task is added succesfully")
    
    def view_tasks(self):
        for task in self.tasks:
            print(task.to_dict())
    
    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        for task in self.tasks:
            if task.task_id == task_id:
                if title:
                    task.title = title
                if description:
                    task.description = description
                if due_date:
                    task.due_date = due_date
                if status:
                    task.status = status
                print("Task updated successfully!")
                return
        print("Task not found!")
    
    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!")
    
    def filter_tasks(self, status):
        filtered_tasks = [task for task in self.tasks if task.status == status]
        for task in filtered_tasks:
            print(task.to_dict())
    
    def save_tasks(self):
        self.file_storing.save(self.tasks)
        print("Tasks saved successfully!")


if __name__ == "__main__":
    storage = JSONFileStoring()  
    app = ToDoProg(storage)
    
    while True:
        print("\nWelcome to the To-Do Application!")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Save tasks")
        print("7. Exit")
        choice = input("Enter your choice: ")
        try:
            if choice == '1':
                task_id = input("Enter Task ID: ")
                title = input("Enter Title: ")
                description = input("Enter Description: ")
                due_date = input("Enter Due Date (YYYY-MM-DD, optional): ") or None
                status = input("Enter Status (In Progress/Completed): ")
                app.add_task(Task(task_id, title, description, due_date, status))
            elif choice == '2':
                app.view_tasks()
            elif choice == '3':
                task_id = input("Enter Task ID to update: ")
                title = input("Enter new Title (or press Enter to skip): ") or None
                description = input("Enter new Description (or press Enter to skip): ") or None
                due_date = input("Enter new Due Date (YYYY-MM-DD, or press Enter to skip): ") or None
                status = input("Enter new Status (Pending/In Progress/Completed, or press Enter to skip): ") or None
                app.update_task(task_id, title, description, due_date, status)
            elif choice == '4':
                task_id = input("Enter Task ID to delete: ")
                app.delete_task(task_id)
            elif choice == '5':
                status = input("Enter Status to filter by (In Progress/Completed): ")
                app.filter_tasks(status)
            elif choice == '6':
                app.save_tasks()
            elif choice == '7':
                break
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Invalid Value, please enter number!")


        