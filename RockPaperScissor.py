'''
Author : Mr.Aryan
Game-Name : Rock-Paper-Scissor
'''

import random

def dicison(Fplayer, Splayer):
    if (Fplayer == 1 and Splayer == 2) or (Fplayer == 2 and Splayer == 3) or (Fplayer == 3 and Splayer == 1):
        return True

c=u=0

while True:
    
    print("\nPress 0 for Exit\n")
    print("Press 1 for Rock")
    print("Press 2 for Paper")
    print("Press 3 for Scissor\n")
    computer = random.randint(1, 3)
    user = int(input("Enter Your Choice : "))
    if user==computer:
        print("It's a Tie.\n")
    elif dicison(computer, user):
        u+=1
        print(f"You Win {u} Time.")
    elif dicison(user, computer):
        c+=1
        print(f"Computer Win {c} Time.")
    elif user==0:
        break
    else:
        print("Please Enter Valid Input.")
