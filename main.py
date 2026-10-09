import json
# Load employee data from the JSON file
try:
    with open("employees.json", "r", encoding="utf-8") as file:
        employees = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    employees = []

# Save employee data to the JSON file
def save_employees():
    with open("employees.json", "w", encoding="utf-8") as file:
        json.dump(employees, file, indent=4)

# Display the main menu
def display_menu():
    print("Employee Management System")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

# Main program
while True:
    display_menu()
    choice = input("Enter your choice: ").strip()
    # 1. Add Employee
    if choice == "1":
        emp_id = input("Enter Employee ID: ").strip()
        if not emp_id:
            print("Employee ID cannot be empty.")
            continue
        if any(employee.get("id") == emp_id for employee in employees):
            print("Employee ID already exists.")
            continue
        name = input("Enter Employee Name: ").strip()
        if not name:
            print("Employee name cannot be empty.")
            continue
        age = input("Enter Employee Age: ").strip()
        if not age.isdigit() or int(age) <= 0:
            print("Please enter a valid positive age.")
            continue
        position = input("Enter Employee Position: ").strip()
        if not position:
            print("Employee position cannot be empty.")
            continue
        employee = {
            "id": emp_id,
            "name": name,
            "age": int(age),
            "position": position
        }
        employees.append(employee)
        save_employees()
        print("Employee added successfully!")

    # 2. View All Employees
    elif choice == "2":
        if not employees:
            print("No employees found.")
        else:
            print("Employee List")
            for employee in employees:
                print(f"ID: {employee.get('id', 'N/A')}")
                print(f"Name: {employee['name']}")
                print(f"Age: {employee['age']}")
                print(f"Position: {employee['position']}")

    # 3. Search Employee
    elif choice == "3":
        search_id = input("Enter Employee ID to search: ").strip()
        for employee in employees:
            if employee.get("id") == search_id:
                print(" Employee Found")
                print(f"ID: {employee['id']}")
                print(f"Name: {employee['name']}")
                print(f"Age: {employee['age']}")
                print(f"Position: {employee['position']}")
                break
        else:
            print("Employee not found.")

    # 4. Update Employee
    elif choice == "4":
        update_id = input("Enter Employee ID to update: ").strip()
        for employee in employees:
            if employee.get("id") == update_id:
                print("Current Employee Details")
                print(f"Name: {employee['name']}")
                print(f"Age: {employee['age']}")
                print(f"Position: {employee['position']}")
                name = input("Enter New Name: ").strip()
                if not name:
                    print("Name cannot be empty. Update cancelled.")
                    break
                age = input("Enter New Age: ").strip()
                if not age.isdigit() or int(age) <= 0:
                    print("Invalid age.")
                    break
                position = input("Enter New Position: ").strip()
                if not position:
                    print("Position cannot be empty. Update cancelled.")
                    break
                employee["name"] = name
                employee["age"] = int(age)
                employee["position"] = position
                save_employees()
                print("Employee updated successfully!")
                break
        else:
            print("Employee not found.")

    # 5. Delete Employee
    elif choice == "5":
        delete_id = input("Enter Employee ID to delete: ").strip()
        for index, employee in enumerate(employees):
            if employee.get("id") == delete_id:
                print(f"Employee found: {employee['name']}")
                confirm = input("Are you sure you want to delete? (y/n): ")
                if confirm.strip().lower() == "y":
                    del employees[index]
                    save_employees()
                    print("Employee deleted successfully!")
                else:
                    print("Deletion cancelled.")
                break
        else:
            print("Employee not found.")

    # 6. Exit
    elif choice == "6":
        print("Thank you for using Employee Management System!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
