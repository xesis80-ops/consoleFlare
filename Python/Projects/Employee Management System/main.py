class employee:
    def __init__(self,id,name,age,gender,jobpos,salary):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.jobpos = jobpos
        self.salary = salary
    
class manage_employee:
    def __init__(self):
        self.emp_array=[]

    def add_employee(self):
        while True:
            empid = int(input("ID: "))
            if any(emp.id == empid for emp in self.emp_array):
                print("ID exists , Try again")
            else:
                break
        name = str(input("Name: "))
        age = int(input("Age: "))
        gender = str(input("Gender: "))
        jobpos = str(input("Jobpos: "))
        salary = int(input("Salary: "))

        temp = employee(empid,name,age,gender,jobpos,salary)
        self.emp_array.append(temp)
        print ("Employee Added Successfully")
        print()

    def update_employee(self):
        keyid = int(input("Enter the UserID :"))
        temp = None
        for emp in self.emp_array:
            if emp.id == keyid:
                temp = emp
                break
        if temp is None:
            print("Employee doesn't exist!\n")
            print()
            return
        print("Which information you want to update ? \n1.Name\n2.Age\n3.Gender\n4.Position\n5.Salary")
        choice = int(input('Enter your Choice : '))
        if choice == 1:
            print(temp.name)
            temp.name = input("Enter new name: ")
        elif choice == 2:
            print(temp.age)
            temp.age = int(input("Enter new age: "))
        elif choice == 3:
            print(temp.gender)
            temp.gender = input("Enter new gender: ")
        elif choice == 4:
            print(temp.jobpos)
            temp.jobpos = input("Enter new position: ")
        elif choice == 5:
            print(temp.salary)
            temp.salary = int(input("Enter new salary: "))
        else:
            print("Invalid choice")
            print()
            return
        print("Employee details updated successfully")

    def delete_employee(self):
        keyid = int(input("Enter EmployeeID: "))
        temp = None
        for emp in self.emp_array:
            if emp.id == keyid:
                temp = emp
                self.emp_array.remove(emp)
                break
        if temp == None:
            print("Employee Doesn't Exists")
            return    
        print("Employee deleted successfully\n")    

    def list_employees(self):
        if not self.emp_array:
            print("No employees found.\n")
            return
        print("ID\tName\tAge\tGender\tPosition\tSalary")
        print("-" * 70)
        for emp in self.emp_array:
            print(f"{emp.id}\t{emp.name}\t{emp.age}\t{emp.gender}\t{emp.jobpos}\t{emp.salary}")
        print()

def main():
    manager = manage_employee()
    while True:
        print("----Employee Management System-----")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. List Employees")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == None:
            print("Please provide a valid input")
            main()
        elif choice == 1:
            manager.add_employee()
        elif choice == 2:
            manager.update_employee()
        elif choice == 3:
            manager.delete_employee()
        elif choice == 4:
            manager.list_employees()
        elif choice == 5:
            print("Program Exited!!")
            break

if __name__ == "__main__":
    main()