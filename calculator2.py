def calculator():
    

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Division by zero error.")
                return 
            result = num1 / num2
        else:
            print("Invalid operation. Please enter +, -, *, or /.")
            return 

        print("Result:", result)

    except ValueError:
        print("Invalid input. enter a number.")
    except Exception as e: 
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    calculator()