dataset = []
summary = {}
def input_data():
    """Accept data from the user or use sample data."""
    global dataset

    print("\n1. Enter Data Manually")
    print("2. Use Sample Data")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter number of values: "))

        dataset = []

        for i in range(n):
            value = int(input("Enter value: "))
            dataset.append(value)

    elif choice == 2:
        dataset = [10, 20, 30, 40, 50]

    else:
        print("Invalid choice!")

    print("Dataset:", dataset)


def display_summary():
    """Display basic statistics using built-in functions."""
    global summary

    if len(dataset) == 0:
        print("Please enter data first!")
        return

    total = sum(dataset)
    average = total / len(dataset)

    summary = {
        "Total Values": len(dataset),
        "Sum": total,
        "Minimum": min(dataset),
        "Maximum": max(dataset),
        "Average": average
    }

    show_summary(**summary)


def show_summary(**kwargs):
    """Display dataset summary."""
    print("\nData Summary:")

    for key, value in kwargs.items():
        print(key, ":", value)


def factorial(n):
    """Calculate factorial using recursion."""

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


def calculate_factorial():
    """Take input and display factorial."""

    n = int(input("Enter a number: "))

    if n < 0:
        print("Factorial is not possible for negative numbers.")

    elif n > 100:
        print("Please enter a number up to 100.")

    else:
        print("Factorial:", factorial(n))


def filter_data():
    """Filter values using lambda and filter."""

    if len(dataset) == 0:
        print("Please enter data first!")
        return

    limit = int(input("Enter threshold value: "))

    result = list(filter(lambda x: x > limit, dataset))

    print("Values greater than", limit, ":", result)


def sort_data():
    """Sort data in ascending and descending order."""

    if len(dataset) == 0:
        print("Please enter data first!")
        return

    print("\n1. Ascending Order")
    print("2. Descending Order")

    choice = int(input("Enter choice: "))

    if choice == 1:
        dataset.sort()
        print("Sorted Data:", dataset)

    elif choice == 2:
        dataset.sort(reverse=True)
        print("Sorted Data:", dataset)

    else:
        print("Invalid choice!")


def dataset_statistics():
    """Return minimum, maximum and average values."""

    if len(dataset) == 0:
        print("Please enter data first!")
        return

    minimum = min(dataset)
    maximum = max(dataset)
    average = sum(dataset) / len(dataset)

    return minimum, maximum, average


def display_statistics():
    """Display multiple returned statistics."""

    result = dataset_statistics()

    if result is not None:
        minimum, maximum, average = result

        print("Minimum:", minimum)
        print("Maximum:", maximum)
        print("Average:", average)


def main():
    """Display the main menu of the program."""

    print("\nWelcome to the Data Analyzer and Transformer Program")

    while True:

        print("\n========== MAIN MENU ==========")
        print("1. Input Data")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple Values)")
        print("7. Exit Program")

        choice = int(input("Please enter your choice: "))

        if choice == 1:
            input_data()

        elif choice == 2:
            display_summary()

        elif choice == 3:
            calculate_factorial()

        elif choice == 4:
            filter_data()

        elif choice == 5:
            sort_data()

        elif choice == 6:
            display_statistics()

        elif choice == 7:
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice! Please try again.")

main()