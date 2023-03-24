'''Write a program which let user to check their lucky draw tickets
 (4 digit number) for prize winning. Each user is given 3 chances
 to key in ticket numbers. If the ticket number is 1888,
 display that user has won grand prize RM1 million, else if the
 ticket number is 5888, display that user has won special prize
 of RM5000, else if the ticket number is 8999, display that
  user has won consolation prize of RM199. Display
  no winning message if the ticket number does not match
  with winning number. In addition, add break to quit the
  loop if the user has won a prize.
'''

counter=1
while(counter<=3):
    ticketNum=int(input("Enter the ticket number"))
    if(ticketNum==1888):
        print("Prize is RM1 million")
        break
    elif(ticketNum==5888):
        print("Prize is RM5000")
        break
    elif (ticketNum == 8999):
        print("Prize is RM199")
        break
    counter=counter+1