import math
def add(x, y):
        return x + y
def subtract(x, y):
        return x - y
def multiply(x, y):
       return x * y
def divide(x, y):
        if y == 0:
            raise ValueError("Can't divide with zero")
        return x / y
def calculate():
    print("""
    Select operation:
    1.Add
    2.Subtract
    3.Multiply
    4.Divide
    """)

    choice = input("Enter choice (1/2/3/4): ")
    while choice not in ["1", "2", "3", "4"]:
        print("Invalid choice!")
        choice = input("Enter choice (1/2/3/4): ")
    choice = int(choice)

    num1 = input("Enter first number: ")
    while not num1.isnumeric():
        print("Invalid input!")
        num1 = input("Enter first number: ")
    num1 = float(num1)

    num2 = input("Enter second number: ")
    while not num2.isnumeric():
        print("Invalid input!")
        num2 = input("Enter second number: ")
    num2 = float(num2)

    result = 0
    if choice == 1:
        result = add(num1, num2)
    elif choice == 2:
        result = subtract(num1, num2)
    elif choice == 3:
        result = multiply(num1, num2)
    else:
        try:
            result = divide(num1, num2)
        except ValueError:
                return
        
    print(f"Result is: {result:.2f}")

    choice = input("Would you like to do a new calculation? (yes/no): ")
    while choice not in ["yes", "no"]:
        print("Invalid choice!")
        choice = input("Would you like to do a new calculation? (yes/no): ")
    if choice == "yes":
        calculate()
    else:
        print("Goodbye!")
calculate()
