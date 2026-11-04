
# ATM Menu-Driven Banking Simulation

balance = 10000

print("================================")
print("       WELCOME TO ATM")
print("================================")

while True:
    print("\n------ ATM MENU ------")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Mini Statement")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAvailable Balance: Rs.", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Money Deposited Successfully!")
            print("Updated Balance: Rs.", balance)
        else:
            print("Invalid Deposit Amount!")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid Withdrawal Amount!")

        elif amount > balance:
            print("Insufficient Balance!")

        else:
            balance -= amount
            print("Withdrawal Successful!")
            print("Remaining Balance: Rs.", balance)

    elif choice == "4":
        print("\n----- MINI STATEMENT -----")
        print("Current Balance: Rs.", balance)
        print("--------------------------")

    elif choice == "5":
        print("\nThank You for Using Our ATM!")
        print("Please Visit Again.")
        break

    else:
        print("Invalid Choice! Please Try Again.")

print("\n===== TRANSACTION COMPLETED =====")
