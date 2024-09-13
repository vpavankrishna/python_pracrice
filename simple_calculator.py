def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select an operation:")
    print("Addition (+)")
    print("Subtraction (-)")
    print("Multiplication (*)")
    print("Division (/)")

    while True:
        choice = input("Enter the number corresponding to your operation (+ or - or * or /): ")

        if choice in ['+', '-', '*', '/']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input! Please enter numerical values.")
                continue

            if choice == '+':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '-':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '*':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '/':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")

        else:
            print("Invalid input! Please select a valid operation.")

        # Ask if the user wants to perform another calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if next_calculation != 'yes':
            print("Goodbye!")
            break

# Run the calculator
if __name__ == "__main__":
    calculator()
