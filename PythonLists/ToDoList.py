# Write a program that lets the user create a to-do list by entering tasks.
# Displays the numbered list of tasks after input is completed.
task=[]
#use sentinel controlled loop to get input from user
while True:
    #get input until 'q' is entered
    tasks=input("Enter the task (or 'q' to quit):")
    if(tasks=='q'):
        break
    #add each entry to list
    task.append(tasks)
#use for loop to add each entry in list
print("To Do List:")
#use enumerate to display list item with index
for index,task in enumerate(task):
    print(index+1,". ",task)

