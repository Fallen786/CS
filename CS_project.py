import mysql.connector as mc
mydb = mc.connect(host="localhost",user="root",password="root",database="eSports")
cur = mydb.cursor()
mydb.autocommit = True
if mydb.is_connected():
    print('Succesfully connected')

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
        pass
    elif x=='2':
        pass
    elif x=='3':
        pass
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
        print('''
1. Display upcoming matches
2. Display team score
3. Add a player
4. Edit a team
5. Search a player
6. Update player details
7. Remove a player
8. Exit
''')
    else:
        print("INVALID INPUT! Try Again")
    menu()
menu()
