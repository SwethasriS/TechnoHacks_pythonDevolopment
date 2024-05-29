import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    return math.pow(x, y)

def sqrt(x):
    if x < 0:
        return "Error! Cannot take the square root of a negative number."
    return math.sqrt(x)

def calculate(expression):
    try:
        return eval(expression)
    except ZeroDivisionError:
        return "Error! Division by zero."
    except Exception as e:
        return f"Error! {e}"

def calculator():
    print("Dynamic Calculator")
    print("You can perform operations like:")
    print("Addition: x + y")
    print("Subtraction: x - y")
    print("Multiplication: x * y")
    print("Division: x / y")
    print("Power: x ** y")
    print("Square Root: sqrt(x)")
    print("Parentheses for grouping: (x + y) * z")
    print("Type 'exit' to quit the calculator")
    
    while True:
        expression = input("Enter expression: ")
        if expression.lower() == 'exit':
            break
        elif 'sqrt' in expression:
            try:
                start = expression.find('(') + 1
                end = expression.find(')')
                number = float(expression[start:end])
                print(f"Result: {sqrt(number)}")
            except ValueError:
                print("Invalid input. Please enter a valid number for square root.")
            except Exception as e:
                print(f"Error! {e}")
        else:
            result = calculate(expression)
            print(f"Result: {result}")

if __name__ == "__main__":
    calculator()
