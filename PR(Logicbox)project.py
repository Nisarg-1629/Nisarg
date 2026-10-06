print("*****Welcome to the Pattern Generator and Number Analyzer*****")
print("   ")    
print("***Choose an option***")
print("   ")
while True:
    choice = input("1. Generate a pattern\n2. Analyze range of numbers\n3. Exit\n    \nEnter your option: ")
    if (choice == '1'):
        rows = int(input("Enter rows: "))
        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end="")
            print()
    elif (choice == '2'):
        start = int(input("Enter starting number: "))
        end = int(input("Enter ending number: "))
        for i in range(start, end + 1):
            if(i % 2 == 0):
                print(f"{i} is even")
            else:
                print(f"{i} is odd")
    elif (choice == '3'):
        print("Exiting the program,bye bye see you next time...")
        break
    else:
        print("Invalid choice.")
        break