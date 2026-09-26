balance = 0.0
kyc_documents = {}

def check_balance():
    print("---------------------------------------------------")
    print(f"Your account balance is ₹{balance}")
    print("---------------------------------------------------")

def deposit(money):
    global balance
    if money >= 0:
        balance += money
        float(balance)
        print("---------------------------------------------------")
        print(f"Total ₹{money} is deposited successfully")
        print(f"Your account balance is ₹{balance}")
        print("---------------------------------------------------")
         
    else:
        print("---------------------------------------------------")
        print("Negative amount cannot be deposited")
        print("---------------------------------------------------")

def withdraw(money):
    global balance
    if money >=0:
        if money > balance:
            print("---------------------------------------------------")
            print("Insufficient balance! Cannot Withdrawn.")
            print("Check you balance")
            print("---------------------------------------------------")
            
        else:
            balance -= money
            print("---------------------------------------------------")
            print(f"Total ₹{money} is withdrawn successfully")
            print(f"Your account balance is ₹{balance}")
            print("---------------------------------------------------")
    elif money < 0:
        print("---------------------------------------------------")
        print("Negative money cannot be withdrawed")
        print("---------------------------------------------------")

def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)

def check_kyc():
    if len(kyc_documents) == 0:
        print("---------------------------------------------------")
        print("KYC is not done!")
        print("---------------------------------------------------")
    for doc in kyc_documents:
        print("---------------------------------------------------")
        print(f"{doc}: {kyc_documents[doc]}")  
        print("---------------------------------------------------")
    
if __name__ == "__main__":
    print("---------------------------------------------------")
    print("Welcome to SBI, Aapka Swagat hai SBI mai")
    print("---------------------------------------------------")
    while True:
        print("1.Check your balance")
        print("2.Deposit money")
        print("3.Withdraw money")
        print("4.Check KYC")
        print("5.Update KYC")
        print("6.Quit")
        choice = input("Enter your choice:")

        if choice == "1":
            check_balance()

        elif choice == "2":
            money = float(input("Enter how much to deposit: "))
            deposit(money)

        elif choice == "3":
            money = float(input("Enter how much to withdraw: "))
            withdraw(money)

        elif choice == "4":
            check_kyc()

        elif choice == "5":
            kyc_documents = {}
            no_documents =  int(input("Enter the number of document you want to add:"))
            for i in range(no_documents):
                key = input("Enter the document type:")
                value = input("Enter the number of document:")
                kyc_documents[key] = value
            update_kyc(kyc_documents)
            print("---------------------------------------------------")
            print("KYC updated")
            print("---------------------------------------------------")

        elif choice == "6":
            break

        else :
            print("Invalid Choice! plz try again")
    print("---------------------------------------------------")
    print("Thank you for banking with us!")
    print("---------------------------------------------------")