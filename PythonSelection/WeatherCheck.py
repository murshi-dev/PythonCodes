'''Write a program that accept the current temperature.
    Recommend the action to be taken based on the temperature.
-	Temperature below 20  sweater reminder
-	Temperature between 20 to 27  pleasant weather
-	Temperature above 28  sunglass/eyewear/umbrella reminder
'''
temperature=int(input("Enter the temperature:  "))
if(temperature<=20):

        print("Sweater Reminder ")

elif(temperature>20 and temperature<=27):

        print("Pleasant Weather ")

elif(temperature>=28):

        print("Sunglass reminder")

else:

        print("Enter proper temperature")
