'''
Q5. Write a program that takes a string input from the user and writes it to a
text file.
'''
str=input("Enter a string: ")
outfile=open("output1.txt","w")
print(str,file=outfile)