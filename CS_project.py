
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="Fowl",password="root")
cur = mydb.cursor()
mydb.autocommit = True

cur.execute("create database Pendragon")

cur = mydb.cursor()
cur.execute("show tables")
for i in cur:
    print(i)
