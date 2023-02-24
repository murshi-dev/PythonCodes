#calculates the total amount of a meal purchased at a restaurant.
# The program should ask the user to enter the charge for the food, drink, and dessert.
# Calculate the amount of a 15 percent tip and 7 percent sales tax. Display each of these amounts and the total.
salesTax: float = 0.07
tipsPercent=0.15
foodPrice = float(input("Enter the food price: "))
drinkPrice = float(input("Enter the drink price: "))
dessertPrice = float(input("Enter the dessert price: "))

totalEaten=foodPrice+drinkPrice+dessertPrice

tipsToGive= totalEaten * tipsPercent
salesTaxToPay=totalEaten * salesTax

toPay= totalEaten + tipsToGive+salesTaxToPay
print("Total Eaten",totalEaten)
print("Tips to give", tipsToGive)
print("Sales Tax value", "{:.2f}".format(salesTaxToPay)) #formats to two decimal places
print("Price after tips and tax is ", toPay)