'''Pet Care Center charges clients a daily rate that is based on both the size of the dog and number of days per month
  in a client’s contract. The following table shows the daily rates. Prompt the user to enter a dog’s weight and number
  of days per month needing care, then calculate and display the daily rate and the total for the month (days times the daily rate).
  Repeat the code until the user chooses to exit. Draw flow chart, write pseudocode and python code.
'''
option='y'
while(option=='y' or option=='Y'):
    dogWeight=int(input("Enter the weight of the dog: "))
    noOfDays=int(input("Enter the no of days care required: "))
    if(dogWeight<10):
        if(noOfDays>=1 and noOfDays<=10):
            total=12*noOfDays
        elif(noOfDays>10):
            total=10*noOfDays
    elif(dogWeight>=10 and dogWeight<35):
        if (noOfDays >= 1 and noOfDays <= 10):
            total = 16 * noOfDays
        elif (noOfDays > 10):
            total = 13 * noOfDays
    elif(dogWeight>=35):
        if (noOfDays >= 1 and noOfDays <= 10):
            total = 19 * noOfDays
        elif (noOfDays > 10):
            total = 17 * noOfDays
    print("Total Charges: ",total)
    option=input("Continue(Y/N): ")