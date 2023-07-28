'''Write a program for a college admissions office.
 The user enters a numeric high school grade point average
  (for example, 3.2), and an admission test score. Print the message “Accept” if the student meets either of the following requirements:
-	A grade point average of 3.0 or above and an admission
 test score of at least 60
-	A grade point average below 3.0 and an admission test
score of at least 80
If the student does not meet either of the qualification
criteria, print “Reject”.
Repeat the code until the user chooses to exit.
Draw flow chart, write pseudocode and python code.
'''
option='y'
while(option=='y' or option=='Y'):
    cgpa=float(input("Enter the CGPA score: "))
    testScore=int(input("Enter the admission test score: "))
    if(cgpa>3 and testScore>=60):
        print("Application Accepted!")
    elif(cgpa<=3 and testScore>=80):
        print("Application Accepted!")
    else:
        print("Application Rejected!")
    option=input("Continue(Y/N): ")