count=1
word=input("Enter any word:")
while(count<=10):
   if(word=="pizza"):
       print("Bingo!")
       print("Total attempt is: ",count)
       break
   else:
       word=input("Wrong Guess , Input again.")
   count=count+1
if(count==10):
    print("Game over, total 10 attempts finished!")