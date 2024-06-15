'''Q22. Write a python program that returns the minimum and maximum values
in a list of numbers.
'''
n=int(input("Total numbers in the list: "))
list1=list()
sum=0

for i in range(n):
    num=int(input("Enter number{}:".format(i+1)))
    list1.append(num)

max=min=list1[0]    
for i in list1:
    if i>=max:
        max=i
    if i<=min:
        min=i
print("Maximum value : {} and Minimum value : {}".format(max,min))
