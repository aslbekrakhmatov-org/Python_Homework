import os

def display_menu():
    print("\nMenu:")
    print("1. Add new employee record")
    print("2. View all employee records")
    print("3. Search for an employee by Employee ID")
    print("4. Update an employee's information")
    print("5. Delete an employee record")
    print("6. Exit")

def add_employee():
    with open("employees.txt", "a") as file:
        new_emp_rec = input("Enter Employee ID, Name, Position, Salary (comma-separated): ")
        file.write(new_emp_rec + "\n")
    print("Employee record added successfully.")

def view_employees():
    try:
        with open("employees.txt", "r") as file:
            content = file.read()
            if content:
                print("\nEmployee Records:")
                print(content)
            else:
                print("No employee records found.")
    except FileNotFoundError:
        print("No employee records found.")

def search_employee():
    emp_id = input("Enter the Employee ID to search: ")
    found = False
    try:
        with open("employees.txt", "r") as file:
            for line in file:
                if line.startswith(emp_id + ","):
                    print("Employee Found: " + line.strip())
                    found = True
                    break
        if not found:
            print("No employee found with ID:", emp_id)
    except FileNotFoundError:
        print("No employee records found.")

def update_employee():
    emp_id = input("Enter the Employee ID to update: ")
    found = False
    try:
        with open("employees.txt", "r") as file:
            lines = file.readlines()
        
        with open("employees.txt", "w") as file:
            for line in lines:
                if line.startswith(emp_id + ","):
                    found = True
                    new_info = input("Enter updated Employee ID, Name, Position, Salary: ")
                    file.write(new_info + "\n")
                else:
                    file.write(line)

        if found:
            print("Employee record updated successfully.")
        else:
            print("No employee found with ID:", emp_id)
    except FileNotFoundError:
        print("No employee records found.")

def delete_employee():
    emp_id = input("Enter the Employee ID to delete: ")
    found = False
    try:
        with open("employees.txt", "r") as file:
            lines = file.readlines()
        
        with open("employees.txt", "w") as file:
            for line in lines:
                if not line.startswith(emp_id + ","):
                    file.write(line)
                else:
                    found = True

        if found:
            print("Employee record deleted successfully.")
        else:
            print("No employee found with ID:", emp_id)
    except FileNotFoundError:
        print("No employee records found.")

while True:
    display_menu()
    try:
        choice = int(input("Choose (1-6): "))
        if choice == 1:
            add_employee()
        elif choice == 2:
            view_employees()
        elif choice == 3:
            search_employee()
        elif choice == 4:
            update_employee()
        elif choice == 5:
            delete_employee()
        elif choice == 6:
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 6.")
    except ValueError:
        print("Invalid input! Please enter a number.")