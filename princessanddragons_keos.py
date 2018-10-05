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

def optArray(n, a):
    if n <= 0:
        return -2
    tot = 0
    num = 0
    main = []
    for i in a:
        if tot >= n:
            break
        else:
            tot += i
            num += 1
            main.append(i)
    extra = tot - n
    if extra < 0:
        return -1
    if extra == 0:
        return main
    else:
        for i in range(num, len(a)):
            maxi = 0
            maxiI = -1
            for j in range(len(main)):
                if main[j] - a[i] <= extra:
                    if main[j] - a[i] >= maxi:
                        maxi = main[j] - a[i]
                        maxiI = j
            if maxiI >= 0:
                main[maxiI] = a[i]
                extra = extra - maxi
        return main


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
        while(skill<1 or skill>100000):
            p=int (input("Strength of the dragon between 1 and 100000 "))
        dragon_skill += " " + skill
    dragon_skill.split()
    print(dragon_skill)

