import random
from datetime import date
from colorama import Fore,Style
print(10*"  ","WELCOME TO GUESS THE NUMBER GAME")
print()
play=input("Do you want to play ? (yes/no) ").lower()
if play!="yes":
    print('if you wnat to play type "yes" ')
else:    
 name=input("enter your name: ")
 print("")
 print(f"Date: {date.today()}", 8*"          ",Fore.CYAN,f"user: {name}",Style.RESET_ALL)
 print()
 print("------------------------------------------------------------------------------------------------------------------")
 number=int(input("enter the range..  "))
 random_no=random.randint(0,number)
 guesses=0
 while True:
    guesses+=1
    if guesses>5:
       print(Fore.RED+"You loss"+Style.RESET_ALL)
       print("you crossed the limits ")
       exit()
    guess_number=int(input("guess the number...."))
    if guess_number>random_no:
        print("You guessed the number too High..")

    elif guess_number<random_no:
        print("you guessed the number too low")
    else:
        print("yes !! your guess is right ")
        print("")
        print(10*"   "+Fore.GREEN+"You Won !!"+Style.RESET_ALL)
        print(" ")
        print(f"you found the number in {guesses} guesses ")
        if guesses<=2:
           print(f"{name}, you played Excellent!")
        elif guesses>=2 and guesses<=4:
           print(f"{name},you played average with many guesses , play well next time") 
        else:
           print(Fore.LIGHTGREEN_EX,"POOR playing,play well next time",Style.RESET_ALL)    
           exit() 
          





