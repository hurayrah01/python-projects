def atm():
    balance = 40000
    pin = 1234
    user = int(input("Enter pin:"))

    if user == pin:
        pass
    else:
        print("Wrong pin")
        return
    
    while True:
        print("1-Deposit")
        print("2-Withdraw")
        print("3-Check Balance")
        print("4-Exit")

        choice = input("Enter choice:")

        if choice == "1":
            amount = int(input("Enter amount:"))
            balance += amount
            print(f"Your new balance is {balance}")

        elif choice == "2":
            amount = int(input("Enter amount:"))
            if amount > balance:
                print("Insufficient funds")
            else:
                balance -= amount
                print(f"Your new balance is {balance}")

        elif choice == "3":
            print(f"Your balance is {balance}")
        
        elif choice == "4":
            print("Goodbye")
            break

        else:
            print("Invalid option")

atm()
   