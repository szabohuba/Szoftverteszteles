import math 

# Function to add two numbers 
def add(num1, num2):
    return num1 + num2
  
# Function to subtract two numbers 
def subtract(num1, num2):
    return num1 - num2
  
# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2
  
# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2

# This function takes x to the power of y
def powerOf(num1,num2):
    aux=pow(num1,num2)
    return aux

# This function calculates the square root of x
def square(num1):
    return math.sqrt(num1)



while True:
        print("\n")
        print("\n")
        print("Please select operation:\n" \
                "1. Add\n" \
                "2. Subtract\n" \
                "3. Multiply\n" \
                "4. Divide\n"
                "5. Power of\n"\
                "6. Square root\n")
        
        
        # Take input from the user 
        select = int(input("Select operations form 1, 2, 3, 4, 5, 6 :"))
        
        
        if select == 1:
            number_1 = int(input("Enter first number: "))
            number_2 = int(input("Enter second number: "))  
            print(number_1, "+", number_2, "=", add(number_1, number_2))
        
        elif select == 2:
            number_1 = int(input("Enter first number: "))
            number_2 = int(input("Enter second number: "))
            print(number_1, "-", number_2, "=", subtract(number_1, number_2))
        
        elif select == 3:
            number_1 = int(input("Enter first number: "))
            number_2 = int(input("Enter second number: "))
            print(number_1, "*", number_2, "=", multiply(number_1, number_2))
        
        elif select == 4:
            number_1 = int(input("Enter first number: "))
            number_2 = int(input("Enter second number: "))
            if number_2 != 0:
                print(number_1, "/", number_2, "=", divide(number_1, number_2))
            else:
                print("You can t dvide any number with 0!")
                exit
                

        elif select == 5:
            number_1 = int(input("Enter first number: "))
            number_2 = int(input("Enter second number: "))
            print(number_1, "^", number_2, "=",powerOf(number_1, number_2)) 

        elif select == 6:
            number_1 = int(input("Enter first number: "))
            print(number_1, "square root is", square(number_1))
            
        else:
            print("Invalid input")
       
    