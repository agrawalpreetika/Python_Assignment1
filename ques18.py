'''
Q18. Write a python program that checks if two strings are anagrams of each
other.
'''
str1=input("Enter string: ")
str2=input("Enter string: ")
dict1={}
for i in str1:
    if i not in dict1:
        dict1[i]=1
    else:
        dict1[i]+=1    
dict2={}
for i in str2:
    if i not in dict2:
        dict2[i]=1
    else:
        dict2[i]+=1 
if dict1==dict2:
    print("The two Strings are anagrams")
else:
    print("Two strings are not anagrams")