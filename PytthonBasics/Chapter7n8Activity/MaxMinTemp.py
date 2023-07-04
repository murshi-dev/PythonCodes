'''Calculate the average temperature from the
maximum and minimum temperature entered. '''
#input
maxTemp=float(input("Enter the max temperature: "))
minTemp=float(input("Enter the min temperature: "))
#process
avgTemp=(maxTemp + minTemp) / 2
#output
print("Average temperature of ",maxTemp," and ",minTemp," is ", avgTemp)