from tabulate import tabulate
import mysql.connector
#connection string - used to connect mysql and the python file
con=mysql.connector.connect(host="localhost", user="root", password="root",database="demomysql")
#check if connection is done
if(con):
    print("Connected")
else:
    print("Not Connected")

#function to add/insert records to the users table
def insert(id,name,age):
    reg=con.cursor();#cursor moves the poiinter to the current location
    sql="INSERT INTO users VALUES (%s,%s,%s)"#%s is the runing parameter from mysql table
    user=(id,name,age)
    #run the query
    reg.execute(sql,user)
    #save the result in db with the commit function
    con.commit()

#function to update
def update(name,age,id):
    reg=con.cursor();#cursor moves the poiinter to the current location
    sql="UPDATE users SET name=%s,age=%s where id=%s"#%s is the runing parameter from mysql table
    user=(name,age,id)
    #run the query
    reg.execute(sql,user)
    #save the result in db with the commit function
    con.commit()

#function to delete
def delete(id):
    reg=con.cursor()
    sql="DELETE FROM users WHERE id=%s"
    user=(id,)
    reg.execute(sql,user)
    con.commit()

#function to display data
def select():
    res=con.cursor()
    sql="SELECT * from users"
    res.execute(sql)
    result=res.fetchall()
    #format the results using tabulate
    print(tabulate(result,headers=["ID","NAME","AGE"]))

while True:
    print("1.Insert Data")
    print("2.Update Data")
    print("3.Display Data")
    print("4.Delete Data")
    print("5. Exit")
    choice=int(input("Enter the option: "))
    if(choice ==1):
        id=int(input("Enter the ID: "))
        name=input("Enter the name: ")
        age=int(input("Enter the age: "))
        #call insert function
        insert(id,name,age)
    elif(choice==2):
        id = int(input("Enter the ID to update: "))
        name = input("Enter the name: ")
        age = int(input("Enter the age: "))
        update(name,age,id)
    elif(choice==3):
        select()
    elif(choice==4):
        id=int(input("Enter the ID to delete: "))
        delete(id)
    elif(choice==5):
        quit()
    else:
        print("invalid choice")