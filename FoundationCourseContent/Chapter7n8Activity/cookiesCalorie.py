#A bag of cookies holds 40 cookies. The calorie information on the bag claims that there are 10 servings in the bag and
# that a serving equals 300 calories. Enter the number of cookies he or she actually ate and then reports the number of total calories consumed

numberOfCookies=40
numberOfServings=10
cookiesOneServing=numberOfCookies/numberOfServings
print("Number of cookies in one serving is", cookiesOneServing)
caloriesOneServing=300
oneCookieCalorie=caloriesOneServing/cookiesOneServing
print("Calories in one cookie: ", oneCookieCalorie)

cookiesEaten=int(input("Enter the number of cookies eaten: "))
caloriesGained=cookiesEaten*oneCookieCalorie

print("Calories Gained is ", caloriesGained)



