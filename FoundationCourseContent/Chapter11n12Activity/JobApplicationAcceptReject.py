'''Write a program that accepts or rejects applicants
 for seasonal jobs. To qualify for a job, an applicant
 must be at least 16 years old and have two years’ work
  experience. Additionally, the applicant must either
  be able to lift at least 20 kg or be able to type 50
  words per minute. Accept all relevant data from a user,
  and display an appropriate message. Repeat the code until
  the user chooses to exit. Draw flow chart, write pseudocode
  and python code.'''
option='y'
while(option=='y' or option=='Y'):
    age=int(input("Enter the age of the applicant: "))
    workExp=int(input("Enter the work experience of the applicant: "))
    if(age<16 or workExp<2):
        print("Application rejected due to age or work experience")
    else:
        weightLimit=int(input("Enter the max weight lifting capacity"))
        typingAbility = int(input("Enter the max words typed per minute"))
        if(weightLimit>=20 or typingAbility>=50):
            print("Application Accepted!")
        else:
            print("Application rejected due to weight lifting limit or typing ability")
    option=input("Continue(Y/N): ")