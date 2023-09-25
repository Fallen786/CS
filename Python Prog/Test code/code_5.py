def upcoming_matches():
    t=int(input('Team (1 or 2): '))
    if t==1:
        q_1="SELECT * FROM schedule WHERE Participant='team1'"
    elif t==2:
        q_1="SELECT * FROM schedule WHERE Participant='team2'"
    cur.execute(q_1)
    records = cur.fetchall()
    for row in records:
        print('League:',row[0] )
        print('Date:',row[1] )
        print('Participant:',row[2] )
        print('Prize:',row[3] )
        print()