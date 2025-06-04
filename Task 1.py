# Function to perform basic mathematical operations
def operations(num1, num2):
    print("\n Calculation Results:")
    print(f" Addition: {num1} + {num2} = {num1 + num2}")
    print(f" Subtraction: {num1} - {num2} = {num1 - num2}")
    print(f" Multiplication: {num1} × {num2} = {num1 * num2}")

    # Handling division to avoid division by zero error
    if num2 != 0:
        print(f" Division: {num1} ÷ {num2} = {num1 / num2}")
    else:
        print("Division by zero is undefined!")

# Taking input from the user.
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    operations(num1, num2)
except ValueError:
    print("Invalid input! Please enter numeric values.")