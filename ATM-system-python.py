# initial balnce
balance=10000
# login details
USERNAME="Chaitanya"
PASSWORD="698"
# Function to check balance
def check_balance(balance):
    print(f"\n Your current balnce is:₹{balance}\n")
# Function to deposit the money
def deposit(balance):
    amount=float(input("Enter amount to deposit:₹"))
    if amount<=0:
        print("Invalid deposi amount!")
    else:
        balance+=amount
        print(f"\n₹{amount} deposited succesfully\n")
    return balance
# Function to withdraw money
def withdraw(balance):
    amount=float(input("Enter amount to withdraw: ₹"))
    if amount<=0:
        print("Invalid withdrawal money!")
    else:
        balance-=amount
        print(f"\n₹{amount} withdrawal succesfully\n")
    return balance
# ATM MENU
def atm_menu(balance):
    while True:
        print("====ATM Menu====")
        print("1.Check Balance")
        print("2.Deposit Money")
        print("3.Withdraw Money")
        print("4.Exit")
        choice=input("Choose an option:")
        if choice=='1':
            check_balance(balance)
        elif choice=='2':
            balance= deposit(balance)
        elif choice=='3':
            balance= withdraw(balance)
        elif choice=='4':
            print("\nThanku you for using the ATM\n")
            break
        else:
            print("Invalid option.please try again") 
#login check
def login():
    print("====Welcome to ATM Login====")
    name_input=input("Enter your name:")
    password_input=input("Enter your password:")
    if name_input==USERNAME and password_input==PASSWORD:
        print(f"\nLogin succesfull.Welcome,{USERNAME}\n")
        atm_menu(balance=10000)
    else:
        print("\nLogin failed.invalid name or passwoed.\n")
login()