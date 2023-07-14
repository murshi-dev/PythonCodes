'''Display if a person is eligible for a loan based on the following conditions:
The person’s salary is at least RM 30,000 and that he or she is in the current job for at least two years.
Using Logical operator to write the condition.
'''
salary=int(input("Enter the salary: "))
numYearsWorked=int(input("Enter the number of years worked:"))
if(salary>=30000 and numYearsWorked>=2):
    print("ELIGIBLE for loan")
else:
    print("NOT ELIGIBLE for loan")