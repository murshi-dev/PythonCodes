'''Input a score from user. If the entered score is great than 50 display the grade ‘Pass’ otherwise display ‘Fail’.'''
score=int(input("Enter a score: "))
if(score>=50):
    print(score," is PASS")
else:
    print(score, " is FAIL")
