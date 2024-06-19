
import random

options = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It is a tie!")
    elif player == "rock" and computer == "scissors":
        print("HOORAH!!, You win!")
    elif player == "paper" and computer == "rock":
        print("HOORAH!!, You win!")
    elif player == "scissors" and computer == "paper":
        print("HOORAH!!, You win!")
    else:
        print("OH NO!!, You lose!")

    play_again = input("Do you want to Play Again? (y/n): ").lower() 
    if not play_again == "y":
        running = False

print("Thanks for playing!")
print("MADE BY AAN BUCH")



