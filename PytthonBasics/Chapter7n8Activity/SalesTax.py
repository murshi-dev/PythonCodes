'''Calculate the amount to be paid after sales tax due on a purchase. Sales tax is 6%.'''
#input
amount=float(input("Enter the amount: "))
#process
#assign constant
SALES_TAX=0.06
toPay=amount + (amount * SALES_TAX)
#output
print("Actual amount: ",amount)
print("Amount with tax:", toPay)