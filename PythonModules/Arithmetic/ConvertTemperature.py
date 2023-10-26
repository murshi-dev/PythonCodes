'''Create temperature.py and call the relevant functions to
convert temperatures from Celsius to Fahrenheit'''
import mathOperations
#get input
celsius=float(input("Enter the temperature in Celsius: "))
#call the functions in mathoperations.py to convert temperature partly
partConvert = mathOperations.multiply(celsius,1.8)
tempInFahrenheit=partConvert+32
#print result
print("Converted Temperature: ",tempInFahrenheit)
