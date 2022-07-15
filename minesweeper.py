import random
random_number = random.randint(1, 10)
active_player = 1

while True:
    if active_player == 1:
        print("Player 1")
        p1_input = int(input("Enter a number from 1 to 10 : "))
        if p1_input == random_number:
            print("You lose the game, good luck next time :) ")
            break
        else:
            active_player = 2
    elif active_player == 2:
        print("Player 2")
        p2_input = int(input("Enter a number from 1 to 10 : "))
        if p2_input == random_number:
            print("You lose the game, good luck next time :) ")
            break
        else:
            active_player = 1