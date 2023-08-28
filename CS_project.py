import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="bruh",database="academia")

mycursor = mydb.cursor()
mycursor.execute("show tables")
for i in mycursor:
    print(i)