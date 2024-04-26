# display the amount to be paid after sales tax due on a purchase. Sales tax is 6%.
originalprice = float(input("Enter the original price: "))
salesTax = 0.06  # declare this since this value is provided in question
toPay = originalprice + (originalprice * salesTax)
print("Price after sales tax is ", toPay)
