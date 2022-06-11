import random

while True:

    choices = ["r", "p", "s"]

    computer = random.choice(choices)
    player = input(
        "Whats your choice? 'r' for rock, 'p' for paper, 's' for scissors?: ").lower()

    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("Tie!")

    elif player == "r":
        if computer == "p":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "s":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    elif player == "s":
        if computer == "r":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "p":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    elif player == "p":
        if computer == "s":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "r":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
    elif player != "":
        print("Invalid Selection")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye!")
