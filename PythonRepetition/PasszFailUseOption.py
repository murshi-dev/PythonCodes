'''Display the grade ‘P’ when the score is 60 and greater value otherwise display ‘F’. Repeat the program until users chooses to exit.'''
choice='y'
choice=input("enter a chhoice: ")
while(choice=='y'):
    marks=int(input("enter mark: "))
    if(marks>60):
        print("PASS")
    else:
        print("FAIL")
    choice = input("enter a chhoice: ")