'''
Q25. Write a program that copies the contents of one text file to another.
'''
origfile=open("reading.txt","r")
content=origfile.read()
copyfile=open("output2.txt","w")
copyfile.write(content)