'''Display the voter eligibility based on the following criteria.
Message	                        Criteria
Applicant is too young to vote	Applicant is younger than 18 years old
Applicant can vote	            Applicant is at least 18 years old and have registered to vote
Applicant must register to vote	Applicant is at least 18 years old and have not registered to vote
'''
age=int(input("Enter the age: "))
if(age<18):
    print("Applicant is younger than 18 years old")
else:
    print("Y/y:Yes\t N/n:No")
    regStatus=input("Enter the registration status: ")
    if(regStatus=='Y' or regStatus=='y'):
        print("Applicant is at least 18 years old and have registered to vote")
    else:
        print("Applicant is at least 18 years old and have not registered to vote")

