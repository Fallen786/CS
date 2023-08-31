import mysql.connector as mc
mydb = mc.connect(host="localhost",user="root",password="root",database="eSports")
cur = mydb.cursor()
mydb.autocommit = True
if mydb.is_connected():
    print('Successfully connected')

def upcoming_matches():
    t=int(input('Team (1 or 2): '))
    if t==1:
        q_1="select * from schedule where Participant='team1'"
    elif t==2:
        q_1="select+ * from schedule where Participant='team2'"
    cur.execute(q_1)
    records = cur.fetchall()
    for row in records:
        print('League:',row[0] )
        print('Date:',row[1] )
        print('Participant:',row[2] )
        print('Prize:',row[3] )
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
    records = cur.fetchall()
    for row in records:
        print('Tag:',row[0] )
        print('Player ID:',row[1] )
        print('Role:',row[2] )
        print('Player score:',row[3] )
        print('Player name:',row[4] )
        print('Region:',row[5] )
        print('Regional rank:',row[6] )
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
    q_7_1= f"select tag from information where tag = {rem}"
    cur.execute(q_7_1)
    for i in cur:
        l.append(i[0])
    q_7_2 = f"select tag from team1 where tag = {rem}"
    cur.execute(q_7_2)
    for j in cur:
        l1.append(j[0])
    if l == l1:
        print("Can't execute command because player already exist in a team")
    else:
        q_7 = f"delete from information where tag = {rem}"
        cur.execute(q_7)
        print("Player has been removed successfully.")

def swap():
    print('''
How would you like to swap players?
1. Between Teams
2. From Reserve to Teams
''')
    Ch= int(input("Enter choice: "))
    if Ch == 1:
        xTag=int(input("Enter Tag of player to swap from Team 1: "))
        cur.execute(f'select * from team1 where Tag = {xTag}')
        for i in cur:
            xID= i[1]
            xRole= i[2]
            xScore= i[3]
        yTag=int(input("Enter Tag of player to swap from Team 2: "))
        cur.execute(f'select * from team2 where Tag = {yTag}')
        for j in cur:
            yID= j[1]
            yRole= j[2]
            yScore= j[3]

        q1 = f"Update team1 set Tag={yTag},Player_ID='{yID}',Role='{yRole}',Player_Score={yScore} where Tag = {xTag}"
        q2 = f"Update team2 set Tag={xTag},Player_ID='{xID}',Role='{xRole}',Player_Score={xScore} where Tag = {yTag}"
        cur.execute(q1)
        cur.execute(q2)
        print('Swap Successfull!')
    elif Ch == 2:
        T_Ch= int(input("Swap with Team (1 or 2)?: "))
        if T_Ch == 1:
            team= 'team1'
        elif T_Ch == 2:
            team= 'team2'
        else:
            print("Invalid Input")
        xTag=int(input('Enter Tag of player from team to swap: '))
        zTag=int(input('Enter Tag of reserve to swap: '))
        cur.execute(f"select * from information where Tag = {zTag}")
        for i in cur:
            zID= i[1]
            zRole= i[2]
            zScore= i[3]

        q1 = f"Update {team} set Tag={zTag},Player_ID='{zID}',Role='{zRole}',Player_Score={zScore} where Tag = {xTag}"
        cur.execute(q1)
        print('Swap successfull')

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
        swap()
    elif x=='5':
        search()
    elif x=='6':
        update()
    elif x=='7':
        remove()
    elif x=='8':
        exit()
    elif x.lower()=='guide':
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
