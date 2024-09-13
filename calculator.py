def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    try:
        for num in numbers[1:]:
            result /= num
        return result
    except ZeroDivisionError:
        return "Error! Division by zero."

def get_numbers():
    numbers = input("Enter the numbers separated by spaces: ")
    return [float(num) for num in numbers.split()]

def calculator():
    print("Welcome to the Multiple Number Calculator!")

    while True:
        print("\nOptions:")
        print("Addition")
        print("Subtraction")
        print("Multiplication")
        print("Division")
        print("Exit")

        choice = input("Choose an operation (+,-,*,/) or exit: ")

        if choice == '+':
            numbers = get_numbers()
            print(f"The result of addition is: {add(numbers)}")
        
        elif choice == '-':
            numbers = get_numbers()
            print(f"The result of subtraction is: {subtract(numbers)}")
        
        elif choice == '*':
            numbers = get_numbers()
            print(f"The result of multiplication is: {multiply(numbers)}")
        
        elif choice == '/':
            numbers = get_numbers()
            result = divide(numbers)
            print(f"The result of division is: {result}")
        
        elif choice == 'exit':
            print("calculator was closed")
            break
        
        else:
            print("Invalid choice! Please select a valid option.")

# Run the calculator
if __name__ == "__main__":
    calculator()
