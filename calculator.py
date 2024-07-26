def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! not able to Divide by zero."
    else:
        return x / y

def calculator():
    print("Welcome calculator App!")
    print("Select any one Digit from below:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        # Take input from the user
        choice = input("Enter choice 1 / 2 / 3 / 4) ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")

        else:
            print("Invalid Input ! Please enter a valid choice for operation !")

        # Ask if the user wants to perform another calculation
        next_calculation = input("Do you want to  continue calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

    print("Thanks for using the calculator!")

if __name__ == "__main__":
    calculator()
