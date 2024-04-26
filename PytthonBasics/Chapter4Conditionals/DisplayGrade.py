'''Classify and display a student's grade based on the score.
90 and Greater-A
80 and Greater B
70 and Greater - C
60 and Greater -D
Lesser than 60 -F'''
score=int(input("Enter the score: "))
if(score>90):
    grade='A'
elif(score>80):
    grade='B'
elif(score>70):
    grade='C'
elif(score>60):
    grade='D'
else:
    grade='F'
print("Grade is ",grade)

