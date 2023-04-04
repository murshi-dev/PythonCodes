'''A shop sells books, maps and magazines. Each item is identified
by a unique 4 – digit code. All books have a code starting with 1,
all maps have a code starting with 2 and all magazines have a code
starting with 3. The code 9999 is used to end the algorithm.
Write an algorithm to solve this problem in the form of a flowchart
and pseudocode. Implement in python code which inputs the codes for
all items in stock and outputs the number of books, number of maps
and the number of magazines in stock.
'''

#initialise counter values
books = 5000
maps = 40
magazines = 100
code=int(input("Enter the 4 digit code;Enter 9999 to exit the program"))
if(code>=1000 and code<2000):
	print("Books in stock is ", books)
elif(code>=2000 and code<3000):
	print("Maps in stock is ",maps)
elif(code>=3000 and code<4000):
	print("Magazines in stock is ", magazines)
elif (code == 9999):
	print("End the program")
else:
    print("Code not found")