
# ATM Transaction Sequence Simulation

balance = 10000

print("===== WELCOME TO ATM =====")

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Available Balance: Rs.", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Amount Deposited Successfully!")
            print("Updated Balance: Rs.", balance)
        else:
            print("Invalid Deposit Amount!")

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid Withdrawal Amount!")

        elif amount > balance:
            print("Insufficient Balance!")

        else:
            balance -= amount
            print("Withdrawal Successful!")
            print("Remaining Balance: Rs.", balance)

    elif choice == 4:
        print("Thank You for Using ATM!")
        break

    else:
        print("Invalid Choice! Please Try Again.")

print("===== TRANSACTION COMPLETED =====")
