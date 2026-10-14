students = []
student_data = {}
subjects = set()

while True:

    print("\n===== STUDENT DATA ORGANIZER =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Subjects")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":

        sid = input("Enter Student ID: ")

        if sid in student_data:
            print("Student ID already exists!")
            continue

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        grade = input("Enter Grade: ")
        dob = input("Enter Date of Birth: ")

        sub = input("Enter Subjects (comma separated): ")
        sub_list = sub.split(",")
        sub_list = [s.strip() for s in sub_list]

      
        info = (sid, dob)

       
        details = {
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": sub_list
        }
        student_data[sid] = details
        students.append([info, details])
        for s in sub_list:
            subjects.add(s)

        print("Student added successfully!")

    elif choice == "2":

        if len(students) == 0:
            print("No student records found!")
        else:
            print("\n===== ALL STUDENTS =====")

            for student in students:

                print("Student ID:", student[0][0])
                print("Date of Birth:", student[0][1])
                print("Name: {}".format(student[1]["name"]))
                print("Age: %d" % student[1]["age"])
                print(f"Grade: {student[1]['grade']}")
                print("Subjects:", ", ".join(student[1]["subjects"]))
                print("----------------------")
    elif choice == "3":

        sid = input("Enter Student ID: ")

        if sid in student_data:

            print("1. Update Name")
            print("2. Update Age")
            print("3. Update Grade")
            print("4. Update Subjects")

            ch = input("Enter choice: ")

            if ch == "1":
                student_data[sid]["name"] = input("Enter new name: ")

            elif ch == "2":
                student_data[sid]["age"] = int(input("Enter new age: "))

            elif ch == "3":
                student_data[sid]["grade"] = input("Enter new grade: ")

            elif ch == "4":
                sub = input("Enter new subjects: ")
                sub_list = sub.split(",")
                student_data[sid]["subjects"] = [s.strip() for s in sub_list]

            else:
                print("Invalid choice!")
                continue

        
            for student in students:
                if student[0][0] == sid:
                    student[1].update(student_data[sid])
                    break

            subjects.clear()

            for student in students:
                for s in student[1]["subjects"]:
                    subjects.add(s)

            print("Student updated successfully!")

        else:
            print("Student not found!")

    elif choice == "4":

        sid = input("Enter Student ID: ")

        if sid in student_data:

            for i in range(len(students)):
                if students[i][0][0] == sid:
                    del students[i]
                    break

            del student_data[sid]

            subjects.clear()

            for student in students:
                for s in student[1]["subjects"]:
                    subjects.add(s)

            print("Student deleted successfully!")

        else:
            print("Student not found!")

    elif choice == "5":

        print("\n===== UNIQUE SUBJECTS =====")

        if len(subjects) == 0:
            print("No subjects available!")

        else:
            for s in sorted(subjects):
                print(s)

    elif choice == "6":

        print("Thank you for using Student Data Organizer!")
        break

    else:
        print("Invalid choice! Please try again.")
