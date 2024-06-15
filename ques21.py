'''
Q21. Write a python program that counts the occurrences of a specific element
in a list.
'''
n=int(input("Total elements in the list: "))
list1=list()
sum=0
for i in range(n):
    num=input("Enter element {}:".format(i+1))
    list1.append(num)
element=input("Enter the element:")
count=0
for i in list1:
    if i.lower()==element.lower():
        count+=1
print("the element {} occurs {} times in te given string".format(element,count))
    