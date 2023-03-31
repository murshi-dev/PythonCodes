'''
You are required to get 2 input from the user: their age and their gender.
Show the reward amount which the user entitled as follow:
Age >= 60 and female: RM250
Age >=60 and male: RM300
Age <60 and female: RM200
Age <60 and male: RM150
Prompt the user whether they want to continue to use the program or quit it with Y or N.
'''
choice='Y'
while(choice=='Y'):
    age=int(input("Enter the age: "))
    gender=input("Enter the gender: ")
    if(age>=60 and gender == 'F'):
        print("Reward is 250")
    elif(age>=60 and gender =='M'):
        print("Reward is 300")
    elif (age < 60 and gender == 'F'):
        print("Reward is 200")
    elif (age < 60 and gender == 'M'):
        print("Reward is 150")
    print("Continue(Y/N): ")
    choice=input("Enter the choice: ")