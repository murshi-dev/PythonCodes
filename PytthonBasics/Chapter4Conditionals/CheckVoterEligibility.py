# Input applicant's age
age = int(input("Enter applicant's age: "))

# Check eligibility based on age
if age < 18:
    print("Applicant is too young to vote")
elif age >= 18:
    registered = input("Is the applicant registered to vote? (yes/no): ").lower()
    if registered == "yes":
        print("Applicant can vote")
    elif registered == "no":
        print("Applicant must register to vote")
    else:
        print("Invalid input")
