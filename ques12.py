'''
Q12. Write a python program that calculates the sum of the digits of a given
number.
'''
num=int(input("Enter any number:"))
sum=0
while num!=0 :
    dig=num%10
    sum=sum+dig
    num=num//10
print("Sum of digits:",sum)