from tabulate import tabulate
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="root",database="python_db")

if con:
    print("Connected")
else:
    print("Connection error")

def insert(name,age,city):
    res=con.cursor();
    sql="INSERT INTO users (name,age,city) VALUES (%s,%s,%s)"
    user=(name,age,city)
    res.execute(sql,user)
    con.commit()#important to call this for insert update and delete to refelect the changes in db
    print("data inserted")
def update(name,age,city,id):
    res = con.cursor();
    sql = "UPDATE users set name=%s,age=%s,city=%s WHERE id=%s"
    user = (name, age, city,id)
    res.execute(sql, user)
    con.commit()  # important to call this for insert update and delete to refelect the changes in db
    print("data updated")
def select():
    res=con.cursor()#connects pyhton and mysql using the cursor
    sql="SELECT * from users"
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result,headers=["ID","NAME","AGE","CITY"]))
def delete(id):
    res = con.cursor();
    sql = "DELETE from users WHERE id=%s"
    user = (id,)
    res.execute(sql, user)
    con.commit()  # important to call this for insert update and delete to refelect the changes in db
    print("data deleted")

while True:
    print("1.insert Data")
    print("2.update Data")
    print("3.select Data")
    print("4.delete Data")
    print("5.exit")
    choice=int(input("enter choice: "))
    if choice==1:
        name=input("Enter name: ")
        age = input("Enter age: ")
        city = input("Enter city: ")
        insert(name,age,city)
    elif choice == 2:
            id = input("Enter id: ")
            name = input("Enter name: ")
            age = input("Enter age: ")
            city = input("Enter city: ")
            update(name, age, city,id)
    elif choice == 3:
       select()

    elif choice == 4:
       id = input("Enter id: ")
       delete(id)

    elif choice == 5:
         quit()
    else:
        print("invalid selection")









