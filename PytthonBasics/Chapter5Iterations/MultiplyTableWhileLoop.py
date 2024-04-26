'''Create a multiplication table for an entered number a shown below:
1 * 4 = 4
2 * 4 = 8
3 * 4 = 12
.
.
.
10 * 4 = 40
Use While loop.
'''

counter=1
number=int(input("Enter the number to generate table: "))
while(counter<=10):
    print(counter," * ",number," = ",counter*number)
    counter=counter + 1