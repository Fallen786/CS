import mysql.connector as mc
mydb = mc.connect(host="localhost",user="root",password="root",database="eSports")
cur = mydb.cursor()
mydb.autocommit = True

cur.execute("create database Pendragon")

cur.execute("show tables")
for i in cur:
    print(i)