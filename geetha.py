#To create new project
#NAME : GEETHA P
#DATE : 20-JUL-2022
#PROGRAM : A SIMPLE PYTHON PROGRAM
#CAVEATS : NONE
#DATABASE : NONE if there is any DB then kindly mentioned it

#This is a print function for welcome to new project
def Geetha():
    return("Hello from Geetha!")

print("Welcome to New Project")

#PYTHON VARIABLES
num1 = 40
num2 = 50
sum = num1 + num2
print(sum)

#Variable are Case Sentitive
num1 = 50
NUM2 = 10
Num3 = 40
sum = num1 + NUM2 - Num3
print(sum)

#Camel_Case - should start with small letter
sumOfTwoNumbers = 80

#Pascal_Case - should start with capital letter
SumOfTwoNumbers = 100

#Snake_Case - should start with small leter with combination of underscrore
sum_of_two_numbers = 500

#Multiple values we can assign to multiple varaibles in single code
num1, num2, name = 30, 50, "geetha"

#PYTHON Data Types
# str - text
# int, float, complex - number
# list, dictionary, tuples - sequence
# bool - boolean
# bytes, bytesarray - binary
"""
num1 = 78
name = "Geetha"
value = True

#the type function is useful to find the variable name
print(type(num1))
print(type(name))
print(type(value))

#it use to tell the memory location of variable name
print(id(num1))
print(id(name))
print(id(value))

#Simple data type Program
num1 = input("Enter the value of A : ")
print(type(num1))
num2 = input("Enter the value of B : ")
sum = num1 + num2
print(sum)

num1 = int(input("Enter the value of A : "))
num2 = int(input("Enter the value of B : "))
sum = num1 + num2
print(sum)

#Simple program 1
emp1 = int(input("Enter the student result of Tamil : "))
emp2 = int(input("Enter the student result of English : "))
emp3 = int(input("Enter the student result of Maths : "))
total = emp1 + emp2 + emp3
percentage = total/3
print(total)
print(percentage)
"""

#PYTHON OPERATORS
#ARITHMATIC OPERATORS - It is a + (plus), - (minus), / (division), % (modules), * (multiplication)
#ASSIGNMENT OPERATORS - You are assigning a value to the variable. e.g. num1, num2, stu1. etc.
#COMPARISION OPERATORS - Which we are working on the conditional statement ==, !=, >, <, <=, >=
#LOGICAL OPERATORS - In logical operators we have AND, OR, NOT
#IDENTITYE OPERATORS - These kind of operators is used to compare the objects. It checks the identity
#MEMBERSHIP OPERATORS - It is used to check whether the certain members/elements are exist in the list or not.

# Q:- Write a python program to check whether an input is an INTEGER or FLOAT or Not?
value = input("Enter the value of A : ")
print(type(value))
value = int(input("Enter the value of A : "))
print(type(value))

K = ["1", "2", "3"]
print(( ).join. K)

