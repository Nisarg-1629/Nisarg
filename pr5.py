class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Employee(Person):

    # Constructor with default values (Method Overloading)
    def __init__(self, name, age, employee_id=None, salary=0):
        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__salary = salary

    # Getter for Employee ID
    def get_employee_id(self):
        return self.__employee_id

    # Setter for Employee ID
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    # Getter for Salary
    def get_salary(self):
        return self.__salary

    # Setter for Salary
    def set_salary(self, salary):
        self.__salary = salary

    def display(self):
        super().display()
        print("Employee ID:", self.__employee_id)
        print("Salary:", self.__salary)

    def __del__(self):
        pass



class Manager(Employee):

    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    # Method Overriding
    def display(self):
        print("\nManager Details:")
        super().display()
        print("Department:", self.department)



class Developer(Employee):

    def __init__(self, name, age, employee_id, salary,
                 programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    # Method Overriding
    def display(self):
        print("\nDeveloper Details:")
        super().display()
        print("Programming Language:",
              self.programming_language)


print("Is Manager subclass of Employee?",
      issubclass(Manager, Employee))

print("Is Developer subclass of Employee?",
      issubclass(Developer, Employee))


records = []

while True:

    print("\n--- Employee Management System ---")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Create a Developer")
    print("5. Show Details")
    print("6. Update Employee Salary")
    print("7. Remove Employee")
    print("8. Exit")

    choice = input("\nEnter your choice: ")


    if choice == "1":

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))

        person = Person(name, age)
        records.append(person)

        print("\nPerson created successfully!")

    
    elif choice == "2":

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))

        emp = Employee(name, age, emp_id, salary)
        records.append(emp)

        print("\nEmployee created successfully!")

  
    elif choice == "3":

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")

        manager = Manager(name, age, emp_id,
                          salary, department)

        records.append(manager)

        print("\nManager created successfully!")

    
    elif choice == "4":

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        language = input("Enter Programming Language: ")

        developer = Developer(name, age, emp_id,
                              salary, language)

        records.append(developer)

        print("\nDeveloper created successfully!")

   
    elif choice == "5":

        print("\nChoose details to show:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")
        print("4. Developer")
        print("5. All Details")

        sub_choice = input("Enter your choice: ")

        for obj in records:

            if sub_choice == "1" and type(obj) == Person:
                obj.display()

            elif sub_choice == "2" and type(obj) == Employee:
                print("\nEmployee Details:")
                obj.display()

            elif sub_choice == "3" and type(obj) == Manager:
                obj.display()

            elif sub_choice == "4" and type(obj) == Developer:
                obj.display()

            elif sub_choice == "5":
                obj.display()

    
    elif choice == "6":

        emp_id = input("Enter Employee ID: ")

        found = False

        for obj in records:

            if isinstance(obj, Employee):
                if obj.get_employee_id() == emp_id:

                    salary = float(input("Enter New Salary: "))
                    obj.set_salary(salary)

                    print("Salary updated successfully!")
                    found = True
                    break

        if not found:
            print("Employee not found!")

    
    elif choice == "7":

        emp_id = input("Enter Employee ID: ")

        found = False

        for obj in records:

            if isinstance(obj, Employee):
                if obj.get_employee_id() == emp_id:

                    records.remove(obj)
                    print("Employee removed successfully!")
                    found = True
                    break

        if not found:
            print("Employee not found!")

    
    elif choice == "8":

        print("\nExiting the system.")
        print("All resources have been freed.")
        print("Goodbye!")

        break

    else:
        print("Invalid choice! Please try again.")
