'''Write a program that accept a person’s height in meter. Convert the height into cm. after that, based on the height, determine the suitable sport type to the user. Display the recommendation to the user. Then display message end of program.
-	Height below and equal to 150cm  ping pong
-	Height from 151cm to 165cm  badminton
-	Height from 166cm to 180cm  football
-	Height above 180cm  basketball
'''
height=float(input("Enter the height in meter: "))
centimeter=height*100;
if(centimeter<=150):
    print("Recommended Sport is Ping Pong")
elif(centimeter>=151 and centimeter<=165):
    print("Recommended Sport is Badminton")
elif(centimeter>=166 and centimeter<=180):
    print("Recommended Sport is Football")
elif(centimeter >=180):
    print("Recommended Sport is Basketball")

