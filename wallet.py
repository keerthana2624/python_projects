def initializeWallet():
    wallet={"balance":0,"transection_history":[]}
    return wallet
# print(initializeWallet())


def displaybalance(wallet):
    balance=wallet["balance"]
    print(balance)
    return None
# wallet=initializeWallet()
# displaybalance(wallet)

def addfund(wallet,amount):
    if amount<=0:
        print("amount can not be negative or zero")
        return None
    wallet["balance"]+=amount
    wallet["transection_history"].append(amount)
# wallet=initializeWallet()
# amount=200
# addfund(wallet,amount)


def makepayment(wallet,amount):
    if amount<0:
       print("amount should not be zero")
    if wallet["balance"]<amount:
        print("insufient balance")
    wallet["balance"]-=amount
    wallet["transection_history"].append(amount)
# wallet=initializeWallet()
# print(wallet)
# amount=400
# makepayment(wallet,amount)

def transaction_history(wallet):
    print("transection_history")
    for transection in wallet["transection_history"]:
        print(transection)
# wallet=initializeWallet()
# transaction_history(wallet)

def usewallet():
    print("wel come the wallet")
    wallet=initializeWallet()
    while True:
        print("\nmenu")
        print("a:view balance:")
        print("b:Add funds:")
        print("c:Make a payment:")
        print("d:. View transaction history:")
        print("e:Exit:")
        userchoice=input("enter your option:")

        if userchoice=="a":
            displaybalance(wallet)
        if userchoice=="b":
            amount=float(input("enter amount to add"))
            addfund(wallet,amount)
        if userchoice=="c":
            amount=float(input("enter the payment"))
            makepayment(wallet,amount)
        if userchoice=="d":
            transaction_history(wallet)
        if userchoice=="e":
            print("exiting the wallet")
usewallet() 

       
