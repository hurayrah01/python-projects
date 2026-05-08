import random
def play_game():
    secret_number = random.randint(1,100)
    attempts = 0

    while True:
        if attempts == 5:
            print(f"You ran out of attempts. The correct number is {secret_number}")
            break

        guess = int(input("Enter guess:"))
        attempts += 1

        if guess == secret_number:
            print(f"Correct! You got it in {attempts} attempts")
            break
        elif guess > secret_number:
            print("Too high")
        elif guess < secret_number:
            print("Too low")
    
    again = input("Do you want to play the game again? Yes/No:")
    if again == "Yes":
        play_game()
    else:
        print("Goodbye")

play_game()



    

