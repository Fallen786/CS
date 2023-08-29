
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="Fowl",password="root")
cur = mydb.cursor()
mydb.autocommit = True

cur.execute("create database Pendragon")

mycursor = mydb.cursor()
mycursor.execute("show tables")
for i in mycursor:
    print(i)
