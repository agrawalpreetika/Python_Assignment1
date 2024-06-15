'''
Q3. Write a python program that calculates the factorial of a given number.
'''
num=int(input("Enter any number: "))
fact=1
for i in range(num,0,-1):
    fact=fact*i
print(">> factorial of {} is {}".format(num,fact))