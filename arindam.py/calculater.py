# Calculator using functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# Taking input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose an operation:")
print(" Addition (+)")
print(" Subtraction (-)")
print(" Multiplication (*)")
print(" Division (/)")

choice = input("Enter your choice operation: ")

# Calling functions90
if choice == "+":
    print("Result =", add(num1, num2))

elif choice == "-":
    print("Result =", subtract(num1, num2))

elif choice == "*":
    print("Result =", multiply(num1, num2))

elif choice == "/":
    print("Result =", divide(num1, num2))

else:
    print("Invalid choice")