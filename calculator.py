# Program make a simple calculator
import math 

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

# This function takes x to the power of y
def pow(x,y):
    aux=pow(x,y)
    return aux

# This function calculates the square root of x
def square(x):
    return math.sqrt(x)
    




print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Pow")
print("4.Square root")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6): ")

    # check if choice is one of the six options
    if choice in ('1', '2', '3', '4','5','6'):
        
        
        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "/", num2, "=", divide(num1, num2))
            
        elif choice == '5':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "^", num2, "=", pow(num1, num2))
        
        elif choice == '6':
            num1 = float(input("Enter first number: "))
            print("Square root of ",num1, "=", square(num1))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (Y/N): ")
        if next_calculation == "N":
          break
    
    else:
        print("Invalid Input")