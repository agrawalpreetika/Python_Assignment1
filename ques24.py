'''
Q24. Write a program that acts as a simple calculator. It should take two
numbers and an operator (+, -, *, /) as input and print the result.
'''
num1=float(input("Enter number1: "))
num2=float(input("Enter number2: "))
oper=input("Enter the operator (+, -, /, *): ")

if oper=='+':
    print(num1+num2)
elif oper=='-':
    print(num1-num2)
elif oper=='/':
    print(num1/num2)
elif oper=='*':
    print(num1*num2)
else:
    print(">>Enter Valid Operator<<")    