import random
# Function defined to check either player won or computer


def whowon(comp, player):
    if comp == player:
        print(f"You entered {player} and computer entered {comp} so Tie\n")
    elif comp == 's':
        if player == 'r':
            print(
                f"You entered {player} and computer entered {comp} so you won\n")
        elif player == 'p':
            print(
                f"You entered {player} and computer entered {comp} so Computer won\n")
    elif comp == 'r':
        if player == 's':
            print(
                f"You entered {player} and computer entered {comp} so Computer won\n")

        elif player == 'p':
            print(
                f"You entered {player} and computer entered {comp} so you won\n")
    elif comp == 'p':
        if player == 's':
            print(
                f"You entered {player} and computer entered {comp} so you won\n")
        elif player == 'r':
            print(
                f"You entered {player} and computer entered {comp} so Computer won\n")


# main program
while 1:
    print("Please select one\n 's' for scisor 'r' for rock or 'p' for paper \n Press q to quit\n")
    player = input()
    compin = ("r", "p", "s")
    comp = random.choice(compin)
    if player == 'q':
        print("Leaving the game......")
        break
    else:
        whowon(comp, player)
