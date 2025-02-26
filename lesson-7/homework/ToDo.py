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
        return Task(data["Task ID"], data["Title"], data["Description"], data.get("Due Date"), data["Status"])

class FileStoring(ABC):
    @abstractmethod
    def save(self, tasks):
        pass

    @abstractmethod
    def load(self):
        pass

class CSVFileStoring(FileStoring):
    def __init__(self, filename = "tasks.csv"):
        self.filename = filename

    def save(self, tasks):
        with open(self.filename, '', newline="") as file:
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
        print("Task added successfully.")

    def view_tasks(self):
        if self.tasks:
            for task in self.tasks:
                print(task.to_dict()) 
        else:
            print("No tasks yet")

    def update_task(self, task_id, title=None, description = None, due_date = None, status = None):
        for task in self.tasks:
            if task.task_id == task_id:
                if title:
                    task.title = title
                if description:
                    task.task_desc = description
                if due_date:
                    task.due_date = due_date
                if status:
                    task.status = status
                print("Task is updated successfully!")
                return
            else:
                print("Task with this ID is non found!")
    
    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task with this ID deleted successfully!")
    
    def filter_tasks(self, status):
        filtered_tasks = [task for task in self.tasks if task.status == status]
        for task in filtered_tasks:
            print(task.to_dict())

    def save_tasks(self):
        self.file_storing.save(self.tasks)
        print("Tasks saved successfully")

    


if __name__ == "__main__":
    storage = CSVFileStoring()
    app = ToDoProg(storage)

    while True:
        print("<b>To-Do application</b>")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Save tasks")
        print("7. Exit")

        choice = int(input("Choose option: "))
        try:
            if choice == 1:
                task_id = input("Enter Task ID: ")
                title = input("Enter Title: ")
                task_desc = input("Enter Description: ")
                due_date = input("Enter Due Date (YYYY-MM-DD, optional): ") or None
                status = input("Enter Status (In Progress/Completed): ")
                new_task = Task(task_id, title, task_desc, due_date, status)
                app.add_task(new_task)
            elif choice ==2:
                app.view_tasks()
            elif choice ==3:
                task_id = input("Enter Task ID: ")
                title_updt = input("Enter Title: ") or None
                task_desc_updt = input("Enter Description: ") or None
                due_date_updt = input("Enter Due Date (YYYY-MM-DD, optional): ") or None
                status_updt = input("Enter Status (In Progress/Completed): ") or None
                app.update_task(task_id, title_updt, task_desc_updt, due_date_updt, status_updt)
            elif choice ==4:
                task_id = input("Enter TAsk ID: ")
                app.delete_task(task_id)
            elif choice ==5:
                status = input("Enter the status for filter(In progress/Completed)")
                app.filter_tasks(status)
            elif choice==6:
                app.save_tasks()
            elif choice==7:
                print("App is closed!")
                break
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Invalid Value, please enter number!")