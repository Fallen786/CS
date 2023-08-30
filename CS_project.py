import mysql.connector as mc
mydb = mc.connect(host="localhost",user="root",password="root",database="eSports")
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
    cur.execute(f"Insert into information values({tag},'{pi}','{pn}',{ps},'{rn}',{rr})")

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
        pass
    elif x=='6':
        pass
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