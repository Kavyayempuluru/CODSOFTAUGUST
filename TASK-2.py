# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# This function calculates the power of a number
def power(x, y):
    return x ** y

# This function calculates the modulus of a number
def modulus(x, y):
    return x % y

# This function calculates the square root of a number
def sqrt(x):
    return x ** 0.5

# Print the menu of operations
print("Select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Modulus")
print("7. Square root")

# Take input from the user
choice = input("Enter your choice (1/2/3/4/5/6/7): ")

# Check if the choice is valid
if choice in ("1", "2", "3", "4", "5", "6", "7"):

    # For square root, only one number is needed
    if choice == "7":
        num = float(input("Enter a number: "))
        print(f"The square root of {num} is {sqrt(num)}")
    else:
        # For other operations, two numbers are needed
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform the operation based on the choice and print the result
        if choice == "1":
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == "2":
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == "3":
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == "4":
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == "5":
            print(f"{num1} ^ {num2} = {power(num1, num2)}")
        elif choice == "6":
            print(f"{num1} % {num2} = {modulus(num1, num2)}")

else:
    # If the choice is invalid, print an error message
    print("Invalid input. Please enter a valid choice.")
