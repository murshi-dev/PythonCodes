'''A company has determined that its annual profit is typically 23 percent of total sales.
.Enter the projected amount of total sales, and then displays the profit that will be made from that amount.'''
projectedSales= float(input("Enter the projected amount of total sales: "))
profitRate = 0.23  # declare this since this value is provided in question
profit = projectedSales*profitRate
print('Profit expected is: ', profit)
