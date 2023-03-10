'''Factory Outlet Store is having a sale. All items are on sale with 30% discount
to the original price. The store manager wants a program that allows a sales
clerk to enter the original price of an item and calculate the price after discount.
Also, a fixed sales tax of 6% is charged to the total bill.
Write a program to display the total bill assuming the user purchases three items.
Based on the total bill amount display the following message:

Total bill amount	        Message to display
Rm 250 and greater	        Congrats! You receive RM 20 cash voucher
Between RM 150 to RM 249	Congrats! You receive RM 10 cash voucher
Less than RM 150	        Thank you for shopping with us!
'''
originalPrice1=float(input("Enter the original price of Item 1: "))
originalPrice2=float(input("Enter the original price of Item 2: "))
originalPrice3=float(input("Enter the original price of Item 3: "))

totalOriginalPrice=originalPrice1+originalPrice2+originalPrice3

afterDiscount=totalOriginalPrice-(totalOriginalPrice*0.30)

totalBillAfterSalesTax=afterDiscount+(afterDiscount*0.06)

print("Total bill is: ",totalBillAfterSalesTax)
if(totalBillAfterSalesTax>=250):
    print("Congrats! You receive RM 20 cash voucher")
elif(totalBillAfterSalesTax>=150 and totalBillAfterSalesTax<=249):
    print("Congrats! You receive RM 10 cash voucher")
elif (totalBillAfterSalesTax <150):
    print("Thank you for shopping with us!")
