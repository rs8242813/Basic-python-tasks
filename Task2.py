# Taking user input for first and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Function to generate a friendly greeting
def greet_user(first_name, last_name):
    # Formatting the full name properly
    full_name = f"{first_name} { last_name}"

    # Printing the personalized greeting message
    print(f"\n Hello, {full_name}! Hope you're having an amazing day!")

# Calling the function to display the greeting
greet_user(first_name, last_name)