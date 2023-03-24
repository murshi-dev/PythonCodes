'''Write a program using nested if else structure to determine voter eligibility
based on the following criteria.
Message	Criteria
Applicant is too young to vote	Applicant is younger than 21 years old
Applicant can vote	Applicant is at least 21 years old and have registered to vote
Applicant must register to vote	Applicant is at least 21 years old and have not registered to vote

Assume the voter eligibility must be checked for SEVEN people.
 Use counter controlled repetition structure such that the program
  finds the voter eligibility for SEVEN people.

'''
counter=1
while(counter<=7):
    age=int(input("Enter the applicant age: "))
    if(age>=21):
        reg_status=input("Enter the registration status")
        if(reg_status=='Y'):
            print("Eligible to vote")
        else:
            print("Please register to vote")
    else:
        print("Too young to vote")
    counter=counter+1