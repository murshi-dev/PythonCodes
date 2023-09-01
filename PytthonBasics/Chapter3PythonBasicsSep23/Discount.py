#Calculate the amount to be paid for an apparel with a discount of 20% to its original price.

#input
DISCOUNT=0.20 #assign the constant value
amount=float(input("Enter the amount: "))
#process
toPay=amount-(amount*DISCOUNT)
#output
print("Total To Pay: ",toPay)