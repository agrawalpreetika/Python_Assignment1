'''
Q16. Write a program in python that counts the frequency of each character in
a string.
'''
str1=input("Enter string: ")

dict1={}
for i in str1:
    if i not in dict1:
        dict1[i]=1
    else:
        dict1[i]+=1    
for i in dict1:
    print(i,":",dict1[i])
    