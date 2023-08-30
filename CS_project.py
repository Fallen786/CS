import mysql.connector as mc
mydb = mc.connect(host="localhost",user="Fowl",password="root",database="eSports")
cur = mydb.cursor()
mydb.autocommit = True

cur.execute("desc team1")
for i in cur:
    print(i)
    