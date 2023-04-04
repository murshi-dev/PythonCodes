'''A program takes temperatures input over a 7 day
period (once per day) and outputs the number of days when the
temperature was below 20C
and the number of days when the temperature was 20C and above. '''
below = 0
aboveOrEqual = 0

for i in range(1, 7):
    temperature = float(input("Enter your temperature:"))  # for decimal input
    if (temperature < 20):
        below += 1
    else:
        aboveOrEqual += 1

print("There are ", below, " days was below 20C");
print("There are ", aboveOrEqual, " days was 20C equal and above")
