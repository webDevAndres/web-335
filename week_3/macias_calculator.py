"""
    Title: macias_calculator.py
    Author: Andres Macias
    Date: Aug 28 2022
    Description: Week 3 exercise 3.3 Python Variables and Functions
"""


def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def divide(x,y):
    return x / y

def multiply(x,y):
    return x * y

num1 = 10
num2 = 2

print(num1,"+", num2,"=",add(num1,num2))
print(num1,"-", num2,"=",subtract(num1,num2))
print(num1,"/", num2,"=",divide(num1,num2))
print(num1,"*", num2,"=",multiply(num1,num2))