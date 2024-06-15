'''
Q15. Write a program that reads data from a CSV file and prints it to the
console.
'''
import csv
file=open("csvfile.csv","r")
#creating object read
read=csv.reader(file)
for row in read:
    print(row)


