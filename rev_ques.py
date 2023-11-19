#q- create menu with add,update,delete,display and exit

import mysql.connector as mc
mydb = mc.connect(host="localhost",user="root",password="bruh",database="academia")
mycur = mydb.cursor()
mydb.autocommit = True

def menu():
    x = int(input("1 to add, 2 to update, 3 to delete, 4 to display, 5 to exit: "))
    if x == 1:
        add()
    elif x == 2:
        update()
    elif x == 3:
        delete
    elif x == 4:
        display()
    elif x == 5:
        quit()

def add():
    id = input("Enter id: ")
    name = input("Enter name: ")
    q1 = f"insert into gamer2 values('{id}','{name}')"
    mycur.execute(q1)
def update():
    q = int(input("1 to update id, 2 to update name: "))
    if q == 1:
        id1 = input("ID to change: ")
        id = input("New id: ")
        q2_1 = f"update gamer2 set gamer_id = '{id}' where gamer_id = '{id1}'"
        mycur.execute(q2_1)
    elif q == 2:
        name1 = input("Name to change: ")
        name = input("New name: ")
        q2_2 = f"update gamer2 set gamer_name = '{name}' where gamer_name = '{name1}'"
        mycur.execute(q2_2)

def delete():
    r = input("Enter id to delete: ")
    q3 = f"delete from gamer2 where gamer_id = '{r}'"
    mycur.execute(q3)
    
def display():
    q4 = f"select * from gamer2"
    mycur.execute(q4)

menu()