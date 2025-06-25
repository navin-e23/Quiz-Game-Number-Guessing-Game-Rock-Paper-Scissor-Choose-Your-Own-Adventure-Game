import random
print("welcome to game ")
tc=''' GAME TERMS AND CONDITIONS:
       
         1.Dont cross the game rules like select only (rock/paper/scisors)
         2.paly smoothly
'''
print(tc)
computer_wins=0
user_wins=0
plist=['rock','paper','sciseors']
playing=0
while True:
    playing+=1
    if playing>8:
        print(f"computer score is {computer_wins}")
        print(f"your score is {user_wins}")
        print()
        print(10*" ","GAME OVER")
        exit()
    print("  ")
    user_input=input("====>>> rock/paper/scisors ")
    rand=random.randint(0,2)
    if user_input not in plist:
        print("selected option not in list")
    computer_pick=plist[rand]
    print(f"computer pickes {computer_pick} ")
    if user_input=='rock' and computer_pick=='sciseors':
        print("you won")
        user_wins+=1
    elif user_input=='paper' and computer_pick=="rock"   :
        print("you won!")
        user_wins+=1
    elif user_input=='rock' and computer_pick=='rock':
        print(f"both picks the {user_input} hence both are lose")
    else:
        print("computer won the match ")
        computer_wins+=1
    print(f"Computer score is {computer_wins}")     
    print(f"Your score score is {user_wins}")     
