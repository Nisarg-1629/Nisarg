import os
from datetime import datetime

class JournalManager:

    def __init__(self):
        self.filename = "journal.txt"

    
    def add_entry(self):

        entry = input("Write your journal entry: ")
        date = datetime.now()

        try:
            
            try:
                file = open(self.filename, "x")
                file.close()
            except FileExistsError:
                pass

            
            with open(self.filename, "a") as file:
                file.write("\nDate: " + str(date) + "\n")
                file.write(entry + "\n")

            print("Entry added successfully!")

        except PermissionError:
            print("Permission denied!")

        except Exception as e:
            print("Error:", e)

    
    def view_entries(self):

        try:
            with open(self.filename, "r") as file:
                data = file.read()

                if data == "":
                    print("Journal is empty!")
                else:
                    print("\n--- All Journal Entries ---")
                    print(data)

        except FileNotFoundError:
            print("Journal file does not exist!")

        except PermissionError:
            print("Permission denied!")

    
    def search_entry(self):

        keyword = input("Enter keyword or date to search: ")

        try:
            with open(self.filename, "r") as file:

                data = file.read()

                if keyword.lower() in data.lower():
                    print("\nEntry Found:")
                    print(data)
                else:
                    print("No matching entry found!")

        except FileNotFoundError:
            print("Journal file does not exist!")

        except PermissionError:
            print("Permission denied!")

    
    def delete_entries(self):

        confirm = input("Are you sure? (yes/no): ")

        if confirm.lower() == "yes":

            try:
                
                with open(self.filename, "w") as file:
                    pass

                # Delete file
                os.remove(self.filename)

                print("All entries deleted successfully!")

            except FileNotFoundError:
                print("Journal file does not exist!")

            except PermissionError:
                print("Permission denied!")

        else:
            print("Delete cancelled!")



journal = JournalManager()

while True:

    print("\nWelcome to Personal Journal Manager!")
    print("Please select an option:")

    print("\n1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        journal.add_entry()

    elif choice == "2":
        journal.view_entries()

    elif choice == "3":
        journal.search_entry()

    elif choice == "4":
        journal.delete_entries()

    elif choice == "5":
        print("Thank you for using Personal Journal Manager!")
        break

    else:
        print("Invalid choice! Please try again.")
