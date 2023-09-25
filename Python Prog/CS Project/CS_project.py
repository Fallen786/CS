import mysql.connector as mc
mydb = mc.connect(host="localhost",user="root",password="bruh",database="eSports")
cur = mydb.cursor()
mydb.autocommit = True
if mydb.is_connected():
    print('Succesfully connected')

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
    q_2=f'select sum(Player_Score) from {team}'
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

def swap():
    l = []
    team = ""
    a = int(input("Enter 1 to swap players from team1 or 2 to swap players from team2: "))
    if a == 1:
        team+="team1"
    elif a == 2:
        team+="team2"
    x = input("Enter tag of player to swap: ")
    y = input("Enter tag of player to be swapped with: ")
    q = f"select * from information where tag = {x}"
    cur.execute(q)
    for i in cur:
        for j in range(6):
            l.append(i[j])
    z_0 = l[0]
    z_1 = l[1]
    z_2 = l[2]
    z_3 = l[3]
    z_4 = l[4]
    z_5 = l[5]
    q_4_1 = f"update {team} set player_id = '{z_1}' where tag = {y}"
    cur.execute(q_4_1)
    q_4_2 = f"update {team} set player_name = '{z_2}' where tag = {y}"
    cur.execute(q_4_2)
    q_4_3 = f"update {team} set player_score = {z_3} where tag = {y}"
    cur.execute(q_4_3)
    q_4_4 = f"update {team} set region = '{z_4}' where tag = {y}"
    cur.execute(q_4_4)
    q_4_5 = f"update {team} set regional_rank = {z_5} where tag = {y}"
    cur.execute(q_4_5)
    q_4_0 = f"update {team} set tag = {z_0} where tag = {y}"
    cur.execute(q_4_0)
    print("Players has been swapped successfully.")

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