'''
Game : Guess The Number Between To Numbers For Multiplayer
Author : AJstyles903
'''

import random


def guessing_game(first, second, name, mark):
    for i in range(len(name)):
        count = 0
        print(f"Play the guessing game {name[i]}")
        while True:

            if first < second:
                any = random.randint(first, second)
                break
            elif first > second:
                print(f"Should be {first} < {second} Number.")
                continue
            else:
                print(f"You Don't Insert the Same Value.")
                continue

        while True:

            try:
                guess = int(input(f"Guess The Number {first} Between {second} : "))

            except ValueError:
                print("Please Fill The Integer Value Only.")
                continue

            if first > guess:
                print(f"Please Enter {first} between {second} Numbers")
                continue
            if second < guess:
                print(f"Please Enter {first} between {second} Numbers")
                continue

            if any == guess:
                count += 1
                mark.append(count)
                print(f"{name[i]} finish the game in {count} trial.")
                break
            elif any > guess:
                count += 1
                print(f"Close to the {second} Number.")
            elif any < guess:
                count += 1
                print(f"Close to the {first} Number.")


def Two_Player(player, count):
    if count[0] < count[1]:
        print(f"{player[0]} Win This Game.")
    elif count[0] > count[1]:
        print(f"{player[1]} Win This Game.")
    elif count[0] == count[1]:
        print("Draw the game.")


def Three_Player(player, count):
    if count[0] < count[1] and count[0] < count[2]:
        print(f"{player[0]} Win This Game.")
    elif count[1] < count[0] and count[1] < count[2]:
        print(f"{player[1]} Win This Game.")
    elif count[2] < count[0] and count[2] < count[1]:
        print(f"{player[2]} Win This Game.")
    else:
        print("Draw the game.")


def p_name(length):
    lst = []
    for i in range(length):
        while i < length:
            name = str(input(f"Enter {i+1} Player Name : "))
            if name.isalpha():
                lst.append(name)
                capital = [i.title() for i in lst]
                i += 1
            else:
                print("Please Enter Only String Value In Player Name List.")
        break
    return capital


if __name__ == "__main__":
    while True:
        print("Press 1 To Play The Guessing Game")
        print("Press 2 To Exit The Guessing Game")

        try:
            press = int(input("Please Enter Your Input : "))

        except ValueError:
            print("Please Fill The Integer Value Only.")
            continue

        if press == 1:
            while True:
                try:
                    Start_N = int(input("Enter The Starting Number : "))
                    End_N = int(input("Enter The Ending Number : "))

                except ValueError:
                    print("Please Fill The Integer Value Only.")
                    continue
                while True:
                    print("Press 1 To Play Single Player")
                    print("Press 2 To Play Two Player")
                    print("Press 3 To Play Three Player")
                    try:
                        size = int(input("How Many Player You Won't To Play This Game : "))
                    except ValueError:
                        print("Please Fill The Integer Only.")
                        continue
                    break
                player = []
                player_mark = []

                if size == 1:
                    player_name = p_name(size)
                    guessing_game(Start_N, End_N, player_name, player_mark)

                elif size == 2:
                    player_name = p_name(size)
                    guessing_game(Start_N, End_N, player_name, player_mark)
                    Two_Player(player_name, player_mark)

                elif size == 3:
                    player_name = p_name(size)
                    guessing_game(Start_N, End_N, player_name, player_mark)
                    Three_Player(player_name, player_mark)

                else:
                    print("Please Enter The Valid Input.")
                break
                    
        elif press == 2:
            exit()

        else:
            print("Please Enter The Valid Input.")
