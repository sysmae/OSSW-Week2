# filepath: c:\대학 자료\4-1\오픈소스SW프로젝트\week2\calculator\src\main.py

def add(a, b):
    from operations.add import add as add_func
    return add_func(a, b)

def subtract(a, b):
    from operations.subtract import subtract as subtract_func
    return subtract_func(a, b)

def multiply(a, b):
    from operations.multiply import multiply as multiply_func
    return multiply_func(a, b)

def divide(a, b):
    from operations.divide import divide as divide_func
    return divide_func(a, b)

def main():
    print("Welcome to the Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                if num2 == 0:
                    print("Error! Division by zero.")
                else:
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid Input")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    main()