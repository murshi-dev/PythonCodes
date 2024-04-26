#display the total amount to be paid for an apparel with a discount of 20% to its original price.
originalprice = float(input("Enter the original price: "))
discount = 0.20  # declare this since this value is provided in question
toPay = originalprice - (originalprice * discount)
print("Price after discount tax is ", toPay)