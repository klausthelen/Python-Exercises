print("""
 _   ___                   _____ _          _            
| | / / |                 |_   _| |        | |           
| |/ /| | __ _ _   _ ___    | | | |__   ___| | ___ _ __  
|    \| |/ _` | | | / __|   | | | '_ \ / _ \ |/ _ \ '_ \ 
| |\  \ | (_| | |_| \__ \   | | | | | |  __/ |  __/ | | |
\_| \_/_|\__,_|\__,_|___/   \_/ |_| |_|\___|_|\___|_| |_|
                                                         
                                                         
""")
print("""
/$$   /$$                                                  
| $$  | $$                                                  
| $$  | $$  /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$$
| $$$$$$$$ /$$__  $$ /$$__  $$ /$$_____/ /$$__  $$ /$$_____/
| $$__  $$| $$  \ $$| $$  \__/|  $$$$$$ | $$$$$$$$|  $$$$$$ 
| $$  | $$| $$  | $$| $$       \____  $$| $$_____/ \____  $$
| $$  | $$|  $$$$$$/| $$       /$$$$$$$/|  $$$$$$$ /$$$$$$$/
|__/  |__/ \______/ |__/      |_______/  \_______/|_______/ 
""")
casos = int(input("Number of cases "))
while (casos < 1 or casos > 10):
    casos = int(input("Select a Number of cases between 1 and 10 "))
for t in range(casos):
    n=int (input("Horses in the stable "))
    while (n < 2 or n > 5000):
        n=input("Select a Number of horses between 2 and 5000 ")
    a = ""
    for number in range (n):
        skill = (input("Skill of the horse number " + str(number+1) + " "))
        while (int(skill) < 1 or int(skill) > 1000000000):
            skill=input("The skill number is between 1 and 1000000000 ")
        a += " " + skill
    a=a.split()
    a = [ int(x) for x in a ]
    b=sorted(a)        
    less=1000000000
    less = [abs(int(b[i]) - int(b[i-1])) for i in range(1,len(b))]
    less = sorted(less)[0]
    print("The minimum possible difference is " + str(less))

