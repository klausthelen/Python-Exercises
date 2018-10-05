print("""
 _   ___                   _____ _          _            
| | / / |                 |_   _| |        | |           
| |/ /| | __ _ _   _ ___    | | | |__   ___| | ___ _ __  
|    \| |/ _` | | | / __|   | | | '_ \ / _ \ |/ _ \ '_ \ 
| |\  \ | (_| | |_| \__ \   | | | | | |  __/ |  __/ | | |
\_| \_/_|\__,_|\__,_|___/   \_/ |_| |_|\___|_|\___|_| |_|
                                                         
                                                         
""")
print("""
/$$$$$$$                                                             
| $$__  $$                                                            
| $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$$
| $$  | $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$| $$__  $$ /$$_____/
| $$  | $$| $$  \__/| $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$|  $$$$$$ 
| $$  | $$| $$      | $$  | $$| $$  | $$| $$  | $$| $$  | $$ \____  $$
| $$$$$$$/| $$      |  $$$$$$/|  $$$$$$$|  $$$$$$/| $$  | $$ /$$$$$$$/
|_______/ |__/       \______/  \____  $$ \______/ |__/  |__/|_______/ 
                               /$$  \ $$                              
                              |  $$$$$$/                              
                               \______/                               
""")

from itertools import permutations


def clashes(clash_perm,turn,num_drag,prince_strength):
    cave = 0
    for i in range(num_drag):
        if i>=turn:
            wasteof = sum(clash_perm[int(turn):i+1])
        else:
            wasteof = sum(clash_perm[i:int(turn)+1])
        if wasteof>=prince_strength:
            cave+=1
    return cave


casos = int(input("Number of cases "))
while (casos < 1 or casos > 10):
    casos = int(input("Select a Number of cases between 1 and 10 "))
for t in range(casos): 
    n=int (input("Number of dragons "))
    while(n<1 or n>100000):
        n=int (input("Number of dragons between 1 and 100000 "))
    p=int (input("Prince strength  "))
    while(p<1 or p>100000):
        p=int (input("Prince strength between 1 and 100000 "))
    dragon_skill = ""
    for number in range (n):
        skill = (input("Strength of the dragon " + str(number+1) + " "))
        while(int(skill)<1 or int(skill)>100000):
            skill=(input("Strength of the dragon between 1 and 100000 "))
        dragon_skill += " " + skill
    dragon_skill = dragon_skill.split()
    dragon_skill = [ int(x) for x in dragon_skill ]
    retans = [-1]*n
    dragonsperm = list(permutations(dragon_skill))
    for turn in range(n):
        cave = 0
        for case in dragonsperm:
            cave = max(cave,clashes(case,turn,n,p))
        retans[turn] = cave
    print (' '.join(map(str,retans)))
