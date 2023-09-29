'''Student Info and Grades Tracking
Create a program to track student info – name, id and marks from subjects.
Additionally, calculate and store the average grade for each student.
Hint:
Create a tuple to store each student info as follows:
(name, student_id, grades, average_grade)
Then store these tuples in a list
Display the list.
'''
#create an empty list to store student data
students_list=[]
#set a stop word
sentinel="stop"
#get user input using while loop
while True:
    name=input("Enter student name: ('stop' ends the loop): ")
    if(name==sentinel):
        break;
    id=input("Enter student id: ")
    #use list to get grade inputs
    #create a empty list
    grades=[]
    #get two grades using for loop
    for i in range(2):
        grade=float(input(f"Enter grade for subject {i+1}: "))
        #add this grade input to grades list
        grades.append(grade)
    #use sum() to calculate sum
    # use len() to count the number of grade
    average=sum(grades)/len(grades)
    #now all the input - name,id,grades and average are ready
    #create a tuple with all the info u have
    student_info=(name,id,grades,average)
    #here 'grades' is a list element
    #name,id and average are tuple elements

    #add tuple to the main list
    students_list.append(student_info)

    #display the list
for data in students_list:
    print(f"Name: {data[0]},ID: {data[1]},"
              f"Grades: {data[2]},Average: {data[3]}")
















