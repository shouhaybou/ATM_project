import time as t
# set up the account balance and user pin
pin = int(input("put your pin number: "))
user_pin = pin
user_balance = 97432.50
print("Welcome to Shouhaybou's ATM")
name= input("Enter your Full Name: ")

# setting up to 9 choices
choice = 9
while (True):
    print("\t\t0. Logout and Exit")
    print("\t\t1. View Account Balance")
    print("\t\t2. Withdraw Cash")
    print("\t\t3. Deposit Cash")
    choice = int(input("Enter number to proceed:"))
    print("\n\n")
    
    # checking for the first condition which is the Logout and exit condition
    if choice == 0:
        print("Exiting...")
        t.sleep(2)
        print("You have been logged out. Thank you!\n\n") 
        break
    elif choice in (1,2,3,4,5):
        num_of_tries = 3
        while (num_of_tries!=0):
            input_pin = int(input("Please enter your 4-digit PIN:" ))
            if input_pin == user_pin:
                print("Welcome", name)
                
                # checking the View account balance and the withdraw option
                if choice == 1:
                    print("Loading Account Balance...")
                    t.sleep(1.5)
                    print("Your current balance is:", user_balance, end = "\n\n\n")
                    break
                elif choice == 2:
                    print("Opening Cash Withdrawal...")
                    t.sleep(1.5)
                    
                    while(True):
                        withdraw_amt = float(input("Enter the amount you wish to withdraw:"))
                        if withdraw_amt>user_balance:
                            print("Can't withdraw Rs.", withdraw_amt)
                            print("Please enter a lower amount!")
                            continue
                        else:
                            print("Withdrawing Rs.", withdraw_amt)
                            confirm = input("Confirm? Y/N > ")
                            
                            if confirm in ('Y', 'y'):
                                user_balance-=withdraw_amt
                                print("Amount withdrawn - Rs.", withdraw_amt)
                                print("Remaining balance - Rs.", user_balance, end = "\n\n\n")
                                break
                            else:
                                print("Cancelling transaction...")
                                t.sleep(1)
                                print("Transaction Cancelled!\n\n")
                                break
                    break
                
                #cheking the Deposit Cash option
                elif choice == 3:
                    print("Loading Cash Deposit...")
                    t.sleep(1.5)
                    deposit_amt = float(input("Enter the amount you wish to deposit : "))
                    print("Depositing Rs.", deposit_amt)
                    confirm = input("Confirm? Y/N > ")
                    if confirm in ('Y', 'y'): 
                        user_balance+=deposit_amt
                        print("Amount deposited.", deposit_amt)
                        print("Updated balance.", user_balance, end = "\n\n\n")
                    else:
                        print("Cancelling transaction...")
                        t.sleep(1)
                        print("Transaction Cancelled!\n\n")
                
                                
                    break
                
  


