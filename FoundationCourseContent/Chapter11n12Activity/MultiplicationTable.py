'''Create a multiplication table for an entered number a shown below:
1 * 4 = 4
2 * 4 = 8
3 * 4 = 12
.
.
.
10 * 4 = 40
Write Pseudocode, draw flow chart and python code using for or while loop.
'''
#while loop
counter=1
num = int(input("Enter a number to generate tables: "))
while(counter<=10):
    print(counter," * ",num," = ",counter*num)
    counter=counter+1
