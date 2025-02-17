def display_menu():
    print("Menu:\n")
    print(f"1. Add new employee record\n\
2. View all employee records\n\
3. Search for an employee by Employee ID\n\
4. Update an employee's information\n\
5. Delete an employee record\n\
6. Exit")
    
def add_new_rec():
    new_emp_rec = input("Enter the records of the new employee: ")
    with open("employees.txt", "a") as file:
        file.write(new_emp_rec + "\n")
    print("Records added succesfully")

def view_records():
    try:
        with open("employees.txt") as file:
            recs = file.read()
        if recs:
            print(recs)
        else:
            print("There is no records yet!")
    except FileNotFoundError:
        print("File is not found!")

def search_by_id():
    found = False
    try:
        with open("employees.txt") as file:
            recs = file.readlines()
        if recs:
            emp_id = input("Enter the ID of the employee: ")
            for line in recs:
                if line.startswith(emp_id + ","):
                    found = True
                
            if found:
                line.strip()
                print(line)
            else:
                print("There is no employer with this ID")
        else:
            print("There is no records yet!")
    except FileNotFoundError:
        print("File is not found!")

def update_rec():
    found = False
    updated_recs = []
    with open("employees.txt") as file:
        recs = file.readlines()
    if recs:
        emp_id = input("Enter the ID of the employee: ")
        for line in recs:
            if line.startswith(emp_id + ","):
                found = True
                updt_rec = input("Enter the records for updation: ")
                updated_recs.append(updt_rec + "\n")
            else:
                updated_recs.append(line)
            
            
        if found:
            with open("employees.txt", "w") as for_updt:
                for_updt.writelines(updated_recs)
            print("Record has updated succesfully")
        else:
            print("There is employee with this ID")
    else:
        print("There is no records yet!")

def delete_rec():
    found = False
    updated_recs = []
    with open("employees.txt") as file:
        recs = file.readlines()
    if recs:
        emp_id = input("Enter the ID of the employee: ")
        for line in recs:
            if line.startswith(emp_id + ","):
                found = True
            else:
                updated_recs.append(line)
            
        if found:
            with open("employees.txt", "w") as for_updt:
                for_updt.writelines(updated_recs)
        else:
            print("There is no employee with this ID.")             
    else:
        print("There is no records yet!")
        
def exit_prog():
    print("Exiting the program...")

while True:
    display_menu()
    choice = int(input("Choose the option(1/2/3/4/5/6): "))
    try:
        if choice==1:
            add_new_rec()
        elif choice==2:
            view_records()
        elif choice==3:
            search_by_id()
        elif choice==4:
            update_rec()
        elif choice==5:
            delete_rec()
        elif choice==6:
            exit()
            break
        else:
            print("You chose wrong number. Choose between 1 and 6.")
    except ValueError:
        print("Wrong value. Please enter a number.")


