"""
Calculator Master
A menu-driven calculator built with Git branching.
This is the SKELETON version. The menu loop and input handling exist,
but the actual math operations are added later, one per feature branch.
"""


def get_two_numbers():
    """Ask the user for two numbers, looping until valid input is given."""
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numeric values only.\n")


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def show_menu():
    print("\n===== Calculator Master =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("==============================")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break
        elif choice == "1":
            a, b = get_two_numbers()
            print(f"Result: {add(a, b)}")
        elif choice in ("2", "3", "4"):
            # Placeholder: real operations are added on their own
            # feature branches and merged in here later.
            print("This operation has not been implemented yet.")
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
