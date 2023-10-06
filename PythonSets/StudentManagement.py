#Develop a school management system with the specs provided.

#1.	Subject Offered:
#Each Subject offered by the school can be represented as a set.
# This set would contain the unique student IDs of those enrolled in the Subject.
math_Subject={101,102,103,104,105}
science_Subject={102,104,106,108,110}
history_Subject={101,103,105,107,109}

#2.	Validate Enrollment Validation:
#When a student attempts to enroll in a Subject, check if they are already enrolled in that Subject by using set operations.
student_id=int(input("Enter student id: "))
if student_id in math_Subject:
    print(student_id, " is already enrolled in the maths subject")
else:
        #add the studentid to mats subject
    math_Subject.add(student_id)
    print(student_id, " is successfully registered")
print("Students in Maths: ",math_Subject)

#3.	Subject Intersection:
#Display which Subjects have common students.
common_students=math_Subject & science_Subject
print("Students who take Maths and Science are : ",common_students)
#4.	Removing a Student from a Subject:
#If a student drops a Subject, remove them from the set representing that Subject.
student_id=int(input("Enter student id to remove: "))
if student_id in history_Subject:
    history_Subject.remove(student_id)
    print(student_id, " removed from history subject")
    print("Students in History: ", history_Subject)
else:
    print(student_id, " does not exist in history subject")

#5.	List All Students:
#Create a set of all enrolled students to easily check who is
# enrolled in at least one Subject.
all_students=math_Subject | science_Subject | history_Subject
print("All Students: ", all_students)

#6.	Find all the students who does not have any subject in common
exclusive_students=math_Subject ^ science_Subject ^ history_Subject
print("All Students: ", exclusive_students)