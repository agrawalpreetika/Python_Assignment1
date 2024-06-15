'''
Q26. Write a program in python that checks if a string starts with a given prefix
or ends with a given suffix.
'''

str1=input("Enter a string: ")
prefix=input("Enter the prefix: ")
print("The given string starts with {} :".format(prefix),str1.startswith(prefix))
suffix=input("Enter the suffix: ")
print("The given string ends with {} :".format(suffix),str1.endswith(suffix))