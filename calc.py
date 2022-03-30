import math
from turtle import clear 

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
    if num2 != 0:
        return num1 / num2
    else:
        print("Nem lehet 0-val osztani!")


# This function takes x to the power of y
def powerOf(num1,num2):
    aux=pow(num1,num2)
    return aux

# This function returns the lower number value
def minimum(num1, num2):
    return num1 if num1 <= num2 else num2