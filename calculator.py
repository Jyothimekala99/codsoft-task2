# Function to perform addition
def add(num1, num2):
    return num1 + num2

# Function to perform subtraction
def subtract(num1, num2):
    return num1 - num2

# Function to perform multiplication
def multiply(num1, num2):
    return num1 * num2

# Function to perform division
def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2

# Main calculator function
def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Take user input for operation choice
    choice = input("Enter choice (1/2/3/4): ")

    # Check if the choice is valid
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice")
        return

    # Input two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the selected operation
    if choice == '1':
        result = add(num1, num2)
        print("Result: ", result)
    elif choice == '2':
        result = subtract(num1, num2)
        print("Result: ", result)
    elif choice == '3':
        result = multiply(num1, num2)
        print("Result: ", result)
    elif choice == '4':
        result = divide(num1, num2)
        print("Result: ", result)

# Call the calculator function
calculator()
