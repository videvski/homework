import math

def calculate():
    print('''
    Select operation.
    1.Add
    2.Subtract
    3.Multiply
    4.Divide
    ''')
    choice = input('''Enter choice 1,2,3 or 4: ''')
    while choice not in ['1','2','3','4']:
        print('Invalid choice')
        choice = input('''Enter choice 1,2,3 or 4: ''')
    choice = int(choice)

    x = input('Enter first nubmer:')
    x = float(x)
    y = input('Enter second number:')
    y = float(y)
    
    result=0
    if choice == 1:
        result = x + y
    elif choice == 2:
        result = x - y
    elif choice == 3:
        result = x * y
    elif choice == 4:
        if y == 0:
            print("Can't divide with 0")
        result = x / y
    print(f'Result is {result}')

    choice = input("Would you like to do a new calculation? (yes/no): ")
    while choice not in ["yes", "no"]:
        print("Invalid choice!")
        choice = input("Would you like to do a new calculation? (yes/no): ")
    if choice == "yes":
        calculate()
    else:
        print("Goodbye!")

calculate()
