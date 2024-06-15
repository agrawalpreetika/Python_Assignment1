'''
Q23.  Write a program that converts temperature from Celsius to Fahrenheit
and vice versa based on user input.
'''
temp = float(input("Enter the temperature: "))
scale=input("Enter the temperature scale (F/C): ")
if scale.upper()=='F':
    celsius=5*(temp-32)/9
    print("Corresponding temperature in Celsius:",celsius)
elif scale.upper()=='C':
    fahr=9*temp/5+32
    print("Corresponding temperature in fahrenheit:",fahr)
else:
    print(">>Enter Valid Scale<<")
    
    
    