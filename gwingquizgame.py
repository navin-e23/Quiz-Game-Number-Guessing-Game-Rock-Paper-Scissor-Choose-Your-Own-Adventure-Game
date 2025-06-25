print("")
print(10*"    ","-_-_-_-_-_-_-_-_-_-_-_  QUIZ  _-_-_-_-_-_-_-_-_-_-_-")
while True:
 score=0 
 play=input("=>>DO you want to play (yes/no) ?  ")
 if play!="yes":
     print("if  you have intrest to play enter 'yes', Thank You!! ")
     exit()
 else: 
     print(10*"    ","====..let's play !!..==== ") 
     menu=int(input("enter 1 for menu "))
     if menu!=1:
         print("entered wrong ,please enter 1 next time. ")
     else:
         print("successfully entered!!")    
         print() 
         print("------- MENU --------")
         quiz_topics='''
             1.Maths
             2.Genral Knowledge(GK)
             3.English'''
         print(quiz_topics)
         topic_selection=int(input("select the topic number you have intrest:  "))
         if topic_selection==1:
           print("now answer the maths related questions")
           m1=input("1. A triangle has 3 sides <a=100 degrees ,<b=30 degrees,<c= ______ degrees. ")
           if m1=="50":
              print(f" yes, {m1} correct answer")
              score+=1
           else:
             print(f"{m1} is  wrong answer")    
           m2=input("2. what is the valuse of sin(90)?  ")
           if m2=="1":
             print(f" yes, {m2} correct answer") 
             score+=1   
           else:
             print(f"{m2} is wrong answer")
           m3=input("3. what is the value of x/0__  ") 
           if m3.lower()=="infinity":
             print(f'yes {m3} is correct answer')  
             score+=1   
           else:
             print(f"{m3} is wrong answer ")
             print(f"you gave {score} correct answers")
             print(f"your score is{((score/3)*100)}%")    
         elif topic_selection==2:
            print("selected (GK)")
            g1=input("1. who is the chief minister of telangana?  ")
            if g1.lower()=="reventh reddy":
               print(f"{g1} is correct answer")
               score+=1
            else:
              print(f"{g1} wrong answer")
            g2=input("2. what is national fruit?  ")
            if g2.lower()=="mango":
               print(f"{g2} is correct answer")
               score+=1
            else :
               print(f"{g2} is wrong answer ")
            g3=input("3. who wrote the national antham") 
            if g3.lower()=="rabindranath tagor":
              print(f"{g3} is correct answer") 
              score+=1
            else:
              print(f"{g3} is wrong answer")       
              print(f"you gave {score} correct answers")
              print(f"your score is{((score/3)*100)}%")               
         elif topic_selection==3:
            print("selected English")
            e1=input("1. what _____ you doing ?  ")
            if e1.lower()=="are":
               print(f"{e1} is correct answer")
               score+=1
            else:
               print(f"{e1} is wrong answer")
            e2=input("2. ____ is walking on road. ")
            if e2.lower()=="he" or e2.lower()=="she" or e2.lower()=="it":
               print(f"{e2} is correct answer")
               score+=1
            else:
              print(f'{e2} is wrong answer')
            e3=input("3. I _______ taken lunch. ")
            if e3.lower()=="had":
               print(f"{e3} is correct answer")
               score+=1
            else:
               print(f"{e3} is wrong answer")   
               print(f"you gave {score} correct answers")
               print(f"your score is{((score/3)*100)}%")            
         else:
             print("select correct option...")    
         if score>1:
             print("played well !!")
         elif score==3:
             print(" played excellent")
         else:
             print("dont worry play well next")    
 print("      ")
 print("********Thank you for participating********")