import sys

def enter_pin():
    correct_pin = "1234"

    attempts = 3
    while attempts > 0:
        pin_attempt = str(input("Please enter your 4-digi pin: "))
        if pin_attempt == correct_pin:
            print("Access granted.")
            break
        else:
            attempts -= 1
            print("Incorrect PIN, please try again.")
    else:
        print("Too many incorrect attampts. Goodbye")
        sys.exit()

def withdraw_money():
    global balance
    print("\nHow much would you like to withdraw?\n")
    withdrawal = float(input("> "))
    if withdrawal <= balance:
        balance = balance - withdrawal
        print(f"You now have a balance of £{balance}.")
    else:
        print("You have insufficient funds.")

def deposit_money():
    global balance
    print("\nHow much would you like to deposit?\n")
    deposit = float(input("> "))
    if deposit >= 1:
        balance = balance + deposit
        print(f"You now have balance of £{balance}.")
    else:
        print("You must deposit at least £1.00.")

def display_balance():
    global balance
    print(f"\nYou have a balance of £{balance}.")

balance = float(1000)

enter_pin()
while True:
    print("\nWelcome to Butterfield Bank.\nHow can we help you today?\n")
    print("1. Withraw money\n2. Deposit money\n3. Display balance\n4. Exit\n")
    choice = input("> ")

    if choice == "1":
        withdraw_money()
        
    elif choice == "2":
        deposit_money()

    elif choice == "3":
        display_balance()

    elif choice == "4":
        sys.exit()
        
    else:
        print("Please only use numbers between 1 and 4")