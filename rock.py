import random
choices = ["rock","paper","scissors"]

def play():
    computer = random.choice (choices)
    print(f"Computer chose {computer}")

    user = input("Enter choice:")
    user = user.lower()
    
    if user ==  computer:
        print("It is a draw")

    elif user == "rock" and computer == "scissors":
        print("You win")

    elif user == "paper" and computer == "rock":
        print("You win")

    elif user == "scissors" and computer == "paper":
        print("You win")

    else:
        print("Computer wins")

    again = input("Do you want to play again? yes/no:")
    if again == "yes":
        play()
    
    else:
        print("Goodbye")

play()


