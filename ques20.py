'''
Q20. Write a python program that takes a list of numbers and returns their sum.
'''
n=int(input("Total numbers in the list: "))
list1=list()
sum=0
for i in range(n):
    num=int(input("Enter number{}:".format(i+1)))
    list1.append(num)
    sum+=num
print("The sum of the numbers in given list is:",sum)
    