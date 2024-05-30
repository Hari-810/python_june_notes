def display_menu():
    print("Simple Calculator")
    print("=================")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    else:
        return a / b

def get_numbers():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    return a, b

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            a, b = get_numbers()
            result = add(a, b)
            print(f"The result is: {result}")

        elif choice == '2':
            a, b = get_numbers()
            result = subtract(a, b)
            print(f"The result is: {result}")

        elif choice == '3':
            a, b = get_numbers()
            result = multiply(a, b)
            print(f"The result is: {result}")

        elif choice == '4':
            a, b = get_numbers()
            result = divide(a, b)
            print(f"The result is: {result}")

        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()


"""
How it works:
    display_menu(): Prints the options available to the user.

    add(a, b): Returns the sum of a and b.

    subtract(a, b): Returns the difference between a and b.
    
    multiply(a, b): Returns the product of a and b.
    
    divide(a, b): Returns the quotient of a divided by b, with a check to prevent division by zero.
    
    get_numbers(): Prompts the user to input two numbers and returns them.
    
    main(): The main function that runs an infinite loop to keep the application running until the user decides to quit by choosing option 5. It calls the appropriate function based on the user's choice.
"""

"""

The line if __name__ == "__main__": is a common Python idiom used to ensure that certain code is only executed when the script is run directly, and not when it is imported as a module in another script.


Understanding __name__ and __main__
    __name__: This is a special built-in variable in Python.
    When a Python script is run, the interpreter sets the __name__ variable to "__main__". 
    If the script is being imported into another module, __name__ is set to the name of the script/module.
"""
