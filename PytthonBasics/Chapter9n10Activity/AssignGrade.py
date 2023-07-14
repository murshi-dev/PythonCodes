'''Classify and display a student's grade based on the score.
'''
score=int(input("Enter the score: "))
if(score>90):
    grade='A'
elif(score>80):
    grade='B'
elif (score > 70):
    grade = 'C'
elif (score > 60):
    grade = 'D'
else:
    grade='F'
print("Score is ", score,"\nGrade is ",grade)