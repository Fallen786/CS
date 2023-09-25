import mysql.connector as mc
mydb = mc.connect(host="localhost",user="root",password="bruh",database="eSports")
cur = mydb.cursor()
mydb.autocommit = True

def add_player():
    tag = int(input("Enter tag: "))
    pi = input("Enter player id: ")
    pn = input("Enter player name: ")
    ps = int(input("Enter player score: "))
    rn = input("Enter Region: ")
    rr = int(input("Enter Regional Rank: "))
    q_3 = f"Insert into information values({tag},'{pi}','{pn}',{ps},'{rn}',{rr})"
    cur.execute(q_3)
    print("Player has been added successfully.")

def search():
    s = input("Enter Tag: ")
    q_5 = f"Select * from information where Tag = '{s}'"
    cur.execute(q_5)
    o = cur.fetchall()
    for i in o:
        for a in i:
            print (a,end=", ")
        print()

def update():
    print("Available columns to update: Tag, Player_ID, Player_Name, Player_Score, Region, Regional_Rank")
    col = input("Select column to update: ")
    row = input("Select tag to update: ")
    up = input("Update details: ")
    if col.lower() == "tag" or col.lower() == "player_score" or col.lower() == "regional_rank":
        q_6 = f"Update information set {col} = {up} where tag = {row}"
        cur.execute(q_6)
    elif col.lower() == "player_id" or col.lower() == "player_name" or col.lower() == "region":
        q_6 = f"Update information set {col} = '{up}' where tag = {row}"
        cur.execute(q_6)
    print("Player details has been updated successfully.")

def remove():
    l = []
    l1=[]
    print("Note- Players playing for either teams cannot be removed.")
    rem = int(input("Input Tag of player to be removed: "))
    q_6_1= f"select tag from information where tag = {rem}"
    cur.execute(q_6_1)
    for i in cur:
        l.append(i[0])
    q_6_2 = f"select tag from team1 where tag = {rem}"
    cur.execute(q_6_2)
    for j in cur:
        l1.append(j[0])
    if l == l1:
        print("Can't execute command because player already exist in a team")
    else:
        q_6 = f"delete from information where tag = {rem}"
        cur.execute(q_6)
        print("Player has been removed successfully.")
    
def swap():
    l = []
    team = ""
    a  = int(input("Enter 1 to swap players from team1 or 2 to swap players from team2: "))
    if a == 1:
        team+="team1"
    elif a == 2:
        team+="team2"
    x = input("Enter tag of player to swap: ")
    y = input("Enter tag of player to be swapped with: ")
    q = f"select * from information where tag = {x}"
    cur.execute(q)
    for i in cur:
        for j in range(4):
            l.append(i[j])
    z_0 = l[0]
    z_1 = l[1]
    z_2 = l[2]
    z_3 = l[3]
    q_7_1 = f"update {team} set player_id = '{z_1}' where tag = {y}"
    cur.execute(q_7_1)
    q_7_4 = f"update {team} set role = '{z_2}' where tag = {y}"
    cur.execute(q_7_4)
    q_7_3 = f"update {team} set player_score = {z_3} where tag = {y}"
    cur.execute(q_7_3)
    q_7_0 = f"update {team} set tag = {z_0} where tag = {y}"
    cur.execute(q_7_0)
    print("Players has been swapped successfully.")

swap()
