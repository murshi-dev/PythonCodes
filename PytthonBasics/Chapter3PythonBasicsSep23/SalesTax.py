#Calculate the amount to be paid after sales tax
# #due on a purchase. Sales tax is 6%.

#input
SALES_TAX=0.06 #assign the constant value
amount=float(input("Enter the amount: "))
#process
toPay=amount+(amount*SALES_TAX)
#output
print("Total To Pay: ",toPay)