import mysql.connector as mc
mydb = mc.connect(host="localhost",user="Fowl",password="root")
cur = mydb.cursor()
mydb.autocommit = True

cur.execute("create database Pendragon")

cur.execute("show tables")
for i in cur:
    print(i)