'''
Q19. Write a python program that removes all punctuation from a given string.
'''
punct=[".","?","!",",",";",":","-","_",'"',"'","(",")","[","]","/","...","{","}"]
str2=""
str1=input("Enter a string:")
for i in str1:
    if i not in punct:
        str2+=i
print(str2)

