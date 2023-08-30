import mysql.connector as mc
mydb = mc.connect(host="localhost",user="root",password="bruh",database="eSports")
cur = mydb.cursor()
mydb.autocommit = True
if mydb.is_connected():
    print('Succesfully connected')
    
def upcoming_matches():
    t=int(input('Team (1 or 2): '))
    if t==1:
        q_1="SELECT * FROM schedule WHERE Participant='team1'"
    elif t==2:
        q_1="SELECT * FROM schedule WHERE Participant='team2'"
    cur.execute(q_1)
    o = cur.fetchall()
    for i in o:
        for a in i:
            print (a,end=", ")
        print()

def teamscore():
    t=int(input('Team (1 or 2): '))
    if t==1:
        team='team1'
    elif t==2:
        team='team2'
    q_2=f'SELECT SUM(Player_Score) FROM {team}'
    cur.execute(q_2)
    for i in cur:
        print('For the selected team, the team score will be', i[0])

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

print('''------------------------------
ESPORTS TEAM MANAGEMENT SYSTEM
------------------------------
Welcome
1. Display upcoming matches
2. Display team score
3. Add a player
4. Edit a team
5. Search a player
6. Update player details
7. Remove a player
8. Exit
(To see this guide again, type in 'guide')
''')
def menu():
    x=input('Enter your choice:')
    if x=='1':
        upcoming_matches()
    elif x=='2':
        teamscore()
    elif x=='3':
        add_player()
    elif x=='4':
        pass
    elif x=='5':
        search()
    elif x=='6':
        update()
    elif x=='7':
        pass
    elif x=='8':
        exit()
    elif x=='guide':
        print('''1. Display upcoming matches
2. Display team score
3. Add a player
4. Edit a team
5. Search a player
6. Update player details
7. Remove a player
8. Exit''')
    else:
        print('Invalid option')
    menu()
menu()