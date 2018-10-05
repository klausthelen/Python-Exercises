print("""
 _   ___                   _____ _          _            
| | / / |                 |_   _| |        | |           
| |/ /| | __ _ _   _ ___    | | | |__   ___| | ___ _ __  
|    \| |/ _` | | | / __|   | | | '_ \ / _ \ |/ _ \ '_ \ 
| |\  \ | (_| | |_| \__ \   | | | | | |  __/ |  __/ | | |
\_| \_/_|\__,_|\__,_|___/   \_/ |_| |_|\___|_|\___|_| |_|
                                                         
                                                         
""")
print("""
/$$$$$$$                                /$$   /$$              
| $$__  $$                              | $$  | $$              
| $$  \ $$  /$$$$$$  /$$$$$$$   /$$$$$$ | $$ /$$$$$$   /$$   /$$
| $$$$$$$/ /$$__  $$| $$__  $$ |____  $$| $$|_  $$_/  | $$  | $$
| $$____/ | $$$$$$$$| $$  \ $$  /$$$$$$$| $$  | $$    | $$  | $$
| $$      | $$_____/| $$  | $$ /$$__  $$| $$  | $$ /$$| $$  | $$
| $$      |  $$$$$$$| $$  | $$|  $$$$$$$| $$  |  $$$$/|  $$$$$$$
|__/       \_______/|__/  |__/ \_______/|__/   \___/   \____  $$
                                                       /$$  | $$
                                                      |  $$$$$$/
                                                       \______/  
""")
def winnerfun(teama,teamb):
    if (teama>teamb):
        return('TEAM-A with '+str(teama) + " goals")
    elif (teama<teamb):
        return('TEAM-B with '+str(teamb) + " goals")
    else:
        return(False)


lineofgoals = ""
print("First round of penalty shots")
for i in range(1,11):
    if(i%2):
        input_goal = (input("Shoot " + str(i) + " TEAM-A "))[0]
        lineofgoals += "1" if int(input_goal) > 0 else "0"
    else:
        input_goal = (input("Shoot " + str(i) + " TEAM-B "))[0]
        lineofgoals += "1" if int(input_goal) > 0 else "0"
teama = 0
teamb = 0
i = 0
turns = [5,5]
for shot in lineofgoals:
    if(i%2):
        if(shot!='0'):
            teamb += 1
        turns[0] = turns[0] - 1
        if(teamb + (turns[0]-1) < teama):
            break
    else:
        if(shot!='0'):
            teama += 1
        turns[1] = turns[1] - 1
        if(teama + (turns[1]-1) < teamb):
            break
    i = i+1
i = 0
winner = winnerfun(teama,teamb)
complete_round = 0 
if (winner):
    print(winner)
else:
    print("SUDDEN DEATH")
    while i < 10:
        if(i%2):
            input_goal = (input("Shoot!!!" + str(i+1) + "TEAM-B "))[0]
            if (int(input_goal) > 0):
                teamb += 1
            complete_round += 1
        else:
            input_goal = (input("Shoot!!!" + str(i+1) + "TEAM-A "))[0]
            if (int(input_goal) > 0):
                teama += 1
            complete_round += 1
        if(complete_round == 2):
            winner = winnerfun(teama,teamb)
            complete_round = 0
        if(winner):
            print(winner)
            i = 100
        i = i+1
        if(i != 101):
            print("TIE")



