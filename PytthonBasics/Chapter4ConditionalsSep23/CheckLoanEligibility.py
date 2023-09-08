'''Display if a person is eligible for a loan based on
 the following conditions: The person’s salary is at
 least RM 30,000 and that he or she is in the current
  job for at least two years.
Using Logical operator to write the condition.
'''
salary=int(input("Enter the salary: "))
yearsOnJob=int(input("Enter the number of years in job: "))
#condition using 'and' operator
if(salary>=30000 and yearsOnJob>=2):
    print("Eligible for loan")
else:
    print("Not Eligible for loan")