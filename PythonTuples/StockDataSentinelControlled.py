'''Stock Market Data
Create a program to track stock market data. Each data includes the stock symbol,
current price, and the time of the update.
Hint:
Create a tuple containing the stock symbol, price, and time.
Tuples are suitable for this scenario because once an update
is received, its content must not be changed.
Then Store these tuples in a list.
Display the list. Use sentinel controlled list
'''
#create empty list
stock_data=[]
#create a stop word
sentinel="stop"
#start while
while True:
    # get tuple data from user
    symbol = input("Enter the symbol ('stop' exits the loop): ")
    if symbol==sentinel:
        break;
    #exit the loop when stop is entered
    price=float(input("Enter the price: "))
    time=int(input("Enter the time: "))
    #add/append tuple to list
    stock_data.append((symbol,price,time))
#display list
for data in stock_data:
    print(f"Symbol: {data[0]}, Price: {data[1]},Time: {data[2]}")





