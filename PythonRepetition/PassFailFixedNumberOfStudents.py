'''Display the grade ‘P’ when the score is 60 and greater value
otherwise display ‘F’. Repeat the program to calculate
the result for FIVE students in a class.'''
counter=1
while(counter<=5):
    marks=int(input("enter mark for student"))
    if(marks>60):
        print("PASS")
    else:
        print("FAIL")
    counter=counter+1
