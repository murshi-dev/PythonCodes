#to display the expected weekly pay for next week - raise rate 5%
currentPay= float(input("Enter the current Pay: "))
raiseRate = 0.05  # declare this since this value is provided in question
newPay = currentPay + (currentPay * raiseRate)
print('New pay is: ', newPay)