import os

class employee:
    def __init__(self, id, name, position, salary):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary
    
    def __str__(self):
        return f"{self.id}, {self.name}, {self.position}, {self.salary}"
    
class employee_manager:
    def __init__(self, filename):
        self.filename = filename

    def add_emp(self):
        id = int(input("Enter the ID of new employee: "))
        if self.search_emp_by_id(id, silent=True):
            print("The employee with this ID is already exist")
        
        name = input("Enter the name of new employee: ")
        position = input("Enter the position of new employee: ")
        salary = int(input("Enter the salary of new employee: "))

        with open(self.filename, 'a') as file:
            file.write(f"{id}, {name}, {position}, {salary}\n")
        
        print("Employee has added successfully!")
            
    def view_all_emp(self):
        if not os.path.exists(self.filename):
            print("No records found!")
        
        with open(self.filename, 'r') as file:
            employees = [line.strip().split(", ") for line in file]
        if not employees:
            print("There is no records yet.")
            return

        print("Sort by: ")
        print("1. Name")
        print("2. Salary")
        print("3. No sorting")
        choice = int(input("Choose (1-3):   ").strip())
        
        if choice ==1:
            employees.sort(key= lambda x: x[1])
        elif choice ==2:
            employees.sort(key= lambda x: float(x[3]), reverse=True)
        
        print("Employee records:\n")
        for emp in employees:
            print(", ".join(emp))

    def search_emp_by_id(self, emp_id, silent = False):
        if not os.path.exists(self.filename):
            if not silent:
                print("No record found")
            return None
        
        with open(self.filename, 'r') as file:
            for line in file:
                data = line.strip().split(", ")
                if int(data[0])==emp_id:
                    if not silent:
                        print("\nEmployee is found:")
                        print(line.strip())
                    return data
        if not silent:
            print("No employee found with this ID.")
        return None

    def update_rec(self):
        emp_id = int(input("Enter the ID of employee for updation: "))
        employee_recs = []
        if not os.path.exists(self.filename):
           print("No record found")
           return None
        found = False

        with open(self.filename, 'r') as file:
            for line in file:
                data = line.strip().split(", ")
                if int(data[0])==emp_id:
                    print(f"Employee is found\n {line.strip()}")
                    new_name = input("Update the name: ")
                    new_position = input("Update the position: ")
                    new_salary = int(input("Update the salary: "))
                    employee_recs.append(f"{emp_id}, {new_name}, {new_position}, {new_salary}\n")
                    found = True
                else:
                    employee_recs.append(line)    
        
        if found:
            with open(self.filename, "w") as updt_file:
                updt_file.writelines(employee_recs)
            print("Record has updated succesfully!")
        else:
            print("No employee found with this ID")
            return
        
    def delete_rec(self):
        emp_id = int(input("Enter the ID of the employee for deleting: "))
        employee_recs = []
        if not os.path.exists(self.filename):
            print("No records found!")
            return
        
        found = False
        with open(self.filename, 'r') as file:
            for line in file:
                data = line.strip().split(", ")
                if int(data[0]) == emp_id:
                    found = True
                    continue
                else:
                    employee_recs.append(line)
        
        if found:
            with open(self.filename, 'w') as new_file:
                new_file.writelines(employee_recs)
            print("Employee records has deleted successfully!")           
        else:
            print("Employee not found.")
    
    def menu(self):
        print("\nMenu:")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        while True:
            try:
                choice = int(input("Choose (1-6): "))
                if choice == 1:
                    self.add_emp()
                elif choice == 2:
                    self.view_all_emp()
                elif choice == 3:
                    employee_id = int(input("Enter the ID of employee: "))
                    self.search_emp_by_id(employee_id)
                elif choice == 4:
                    self.update_rec()
                elif choice == 5:
                    self.delete_rec()
                elif choice == 6:
                    exit_prog()
                    break
                else:
                    print("Please enter the numbers between 1 and 6!")
            except ValueError:
                print("Invalid input. Please enter the number!")
def exit_prog():
    print("Program is closed!")



if __name__ == "__main__":
    manager = employee_manager("employees.txt")
    manager.menu()

