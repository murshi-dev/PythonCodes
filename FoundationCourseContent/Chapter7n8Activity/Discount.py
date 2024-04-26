'''Calculate the amount to be paid for an apparel with a discount of 20% to its original price.'''
#input
amount=float(input("Enter the amount: "))
#process
#assign constant
DISCOUNT=0.20
toPay=amount - (amount * DISCOUNT)
#output
print("Actual amount: ",amount)
print("Amount with discount:", toPay)