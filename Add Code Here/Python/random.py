import random
def easy():
    rannum = random.randint(1,10)
    print('''
+-+-+-+-+ +-+-+-+-+
|E|A|S|Y| |M|O|D|E|
+-+-+-+-+ +-+-+-+-+   
''')
    print("Hint: Guess the number between 1 and 10.\n")
    print("Hint: Press 'q' to quit.\n")
    score = 100
    while score>0:
        print(f"your score {score}")
        guess = input("Your Guess:")
        if guess == "":
            print("No guess entered")
            continue
        if guess== "Q" or guess== "q":
            exit()
        guess = int(guess)
        if guess<1 or guess>10:
            print("Out of range")
        elif(guess==rannum):
            return score
        else:
            diff = abs(guess-rannum)
            score -= 3*diff
            if diff == 1:
                print("Very Close")
            elif diff<=3 and diff>1:
                print("Close")
            elif diff<=5 and diff>3:
                print("Far")
            else:
                print("Too far")
            if score<= 0:
                print(f'The random number is {rannum}')    
def medium():
    rannum = random.randint(1,100)
    print('''
+-+-+-+-+-+-+ +-+-+-+-+
|M|E|D|I|U|M| |M|O|D|E|
+-+-+-+-+-+-+ +-+-+-+-+
''')
    print("Hint: Guess the number between 1 and 100.\n")
    print("Hint: Press 'q' to quit.\n")
    score = 1000
    while score>0:
        print(f"your score {score}")
        guess = input("Your Guess:")
        if guess == "":
            print("No guess entered")
            continue
        if guess== "Q" or guess== "q":
            exit()
        guess = int(guess)
        if guess<1 or guess>100:
            print("Out of range")
        elif(guess==rannum):
            return score
        else:
            diff = abs(guess-rannum)
            score -= 6*diff
            if diff <= 10:
                print("Very Close")
            elif diff<=30 and diff>10:
                print("Close")
            elif diff<=50 and diff>30:
                print("Far")
            else:
                print("Too far")
        if score<= 0:
                print(f'The random number is {rannum}')    
def hard():
    rannum = random.randint(1,1000)
    print('''
+-+-+-+-+ +-+-+-+-+
|H|A|R|D| |M|O|D|E|
+-+-+-+-+ +-+-+-+-+
''')
    print("Hint: Guess the number between 1 and 1000.\n")
    print("Hint: Press 'q' to quit.\n")
    score = 10000
    while score>0:
        print(f"your score {score}")
        guess = input("Your Guess:")
        if guess == "":
            print("No guess entered")
            continue
        if guess== "Q" or guess== "q":
            exit()
        guess = int(guess)
        if guess<1 or guess>1000:
            print("Out of range")
        elif(guess==rannum):
            return score
        else:
            diff = abs(guess-rannum)
            score -= 6*diff
            if diff <= 10:
                print("Very Close")
            elif diff<=50 and diff>10:
                print("Close")
            elif diff<=50 and diff>30:
                print("Almost")
            elif diff<100 and diff>50:
                print("far")
            elif diff<200 and diff>100:
                print("too far")
            else:
                print("beyond reach")
        if score<= 0:
                print(f'The random number is {rannum}')    

print(''' ____                 _                 
|  _ \ __ _ _ __   __| | ___  _ __ ___  
| |_) / _` | '_ \ / _` |/ _ \| '_ ` _ \ 
|  _ < (_| | | | | (_| | (_) | | | | | |
|_| \_\__,_|_| |_|\__,_|\___/|_| |_| |_|
                                        
 _   _                 _               
| \ | |_   _ _ __ ___ | |__   ___ _ __ 
|  \| | | | | '_ ` _ \| '_ \ / _ \ '__|
| |\  | |_| | | | | | | |_) |  __/ |   
|_| \_|\__,_|_| |_| |_|_.__/ \___|_|    
                                       
  ____ _           _ _                       
 / ___| |__   __ _| | | ___ _ __   __ _  ___ 
| |   | '_ \ / _` | | |/ _ \ '_ \ / _` |/ _ \\
| |___| | | | (_| | | |  __/ | | | (_| |  __/
 \____|_| |_|\__,_|_|_|\___|_| |_|\__, |\___|
                                  |___/       ''')

res = -1
level = input('''Enter your difficult level:
+-+-+-++-+-+-+-+-+-+-+ 
|EASY| |MEDIUM| |HARD|
+-+-+-++-+-+-+-+-+-+-+
''').lower()
while level == None:
    print("No level is entered")
    continue
if level == "easy":
    res = easy()
elif level =="medium":
     res = medium()
elif level == "hard":
     res = hard()
else:
    print("invalid choice")
    while level.isdigit():
        level = input('''It is a digit 
Please Enter the valid choice:''')

if res == None:
     print('''
  ____    _    __  __ _____    _____     _______ ____  
 / ___|  / \  |  \/  | ____|  / _ \ \   / / ____|  _ \ 
| |  _  / _ \ | |\/| |  _|   | | | \ \ / /|  _| | |_) |
| |_| |/ ___ \| |  | | |___  | |_| |\ V / | |___|  _ < 
 \____/_/   \_\_|  |_|_____|  \___/  \_/  |_____|_| \_\
                                                       
            ''')

elif res>0:
    print('''
 _   _ _   _ ____  ____      _ __   __
| | | | | | |  _ \|  _ \    / \\ \ / /
| |_| | | | | |_) | |_) |  / _ \\ V / 
|  _  | |_| |  _ <|  _ <  / ___ \| |  
|_| |_|\___/|_| \_\_| \_\/_/   \_\_|  
                                      
    ''')
    print(f'You won the game and your score is {res}')

