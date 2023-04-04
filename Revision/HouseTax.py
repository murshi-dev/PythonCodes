'''A town contains 5000 houses. Each house owner must pay tax
based on the value of the house. Houses over RM 200 000 pay
2% of their value in tax, houses over RM 100 000 pay 1.5% of
their value in tax and houses over RM 50 000 pay 1% of their
value in tax. All others pay no tax. '''
amount=int(input("Enter the hous evalue: "))
if(amount>=200000):
   taxToPay=amount*0.02
   print("The amount of tax: ", taxToPay)
elif(amount>=100000 and amount<=199999):
   taxToPay=amount*0.015
   print("The amount of tax: ", taxToPay)
elif(amount>=50000 and amount<= 99999):
   taxToPay = amount * 0.01
   print("Tax Amount: ", taxToPay)
else:
   print("No Tax")
