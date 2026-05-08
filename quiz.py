def quiz():
    score = 0

    question1= ("What is the capital of Nigeria")
    print("A- Abuja")
    print("B- Bayelsa")
    print("C- Cross river")
    print("D- Delta")

    answer1 = input("Enter your answer:")

    if answer1 == "A":
        print("Correct")
        score = score + 1
    else:
        print("Incorrect! The correct answer is A")

    question2 = ("What is the best STEM university in Nigeria")
    print("A- Convenant university")
    print("B- Federal universirt of technology,Akure")
    print("C- Obafemi Awolowo university")
    print("D- University of Ibadan")

    answer2 = input("Enter your answer:")

    if answer2 == "C":
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect! The correct answer is C")

    question3 = ("What is the programming language used in mobile app development")
    print("A- Kotlin")
    print("B- Python")
    print("C- C++")
    print("D- Javascript")

    answer3 = input("Enter your answer:")

    if answer3 == "A":
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect! The correct answer is A")

    question4 = ("Where did anime originate from")
    print("A- America")
    print("B- China")
    print("C- Japan")
    print("D- India")

    answer4 = input("Enter your answer:")

    if answer4 == "C":
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect! The correct answer is C")

    question5 = ("What is the largest ocean in the universe")
    print("A- Pacific ocean")
    print("B- Atlantic ocean")
    print("C- Indian ocean")
    print("D- Artic ocean")

    answer5 = input("Enter your answer:")

    if answer5 == "A":
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect! The correct answer is A")

    print(f"You scored {score} out of 5")

    if score == 3:
        print("Perfect score!")
    elif score == 2:
        print("Good job!")
    else:
        print("Keep studying")

    again = input("Do you want to play again? yes/no")
    if again == "yes":
        quiz()
    else:
        print("Goodbye")

quiz()