'''Stock Market Data
Create a program to track stock market data. Each data includes the stock symbol,
current price, and the time of the update.
Hint:
Create a tuple containing the stock symbol, price, and time.
Tuples are suitable for this scenario because once an update
is received, its content must not be changed.
Then Store these tuples in a list.
Display the list.
'''
#create empty list
stock_data=[]
for i in range(2):
    #get tuple data from user
    symbol=input("Enter the symbol: ")
    price=float(input("Enter the price: "))
    time=int(input("Enter the time: "))
    #add/append tuple to list
    stock_data.append((symbol,price,time))
#display list
for data in stock_data:
    print("Symbol: ",data[0],"Price: ",data[1],"Time: ",data[2])
    #another way to display
    print(f"Symbol: {data[0]}, Price: {data[1]},Time: {data[2]}")





