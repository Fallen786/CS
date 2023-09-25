import mysql.connector as mc
mydb = mc.connect(host="localhost",user="root",password="bruh",database="eSports")
cur = mydb.cursor()
mydb.autocommit = True

def remove():
    l = []
    l1=[]
    l2=[]
    print("Note- Players playing for either teams cannot be removed.")
    rem = int(input("Input Tag of player to be removed: "))
    q_7_1= f"select tag from information where tag = {rem}"
    cur.execute(q_7_1)
    for i in cur:
        l.append(i[0])
    q_7_2_1 = f"select tag from team1 where tag = {rem}"
    q_7_2_2 = f"select tag from team2 where tag = {rem}"
    cur.execute(q_7_2_1)
    for j in cur:
        l1.append(j[0])
    cur.execute(q_7_2_2)
    for j in cur:
        l2.append(j[0])
    if l == l1 or l == l2:
        print("Can't execute command because player already exist in a team")
    else:
        q_7 = f"delete from information where tag = {rem}"
        cur.execute(q_7)
        print("Player has been removed successfully.")


remove()