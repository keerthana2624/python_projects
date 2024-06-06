def initializewallet():
    wallet={"balance":0,"transection_history":[]}
    return wallet
# print(initializewallet())

def displayBalance(wallet):
    balance=wallet["balance"]
    print(balance)
# wallet=initializewallet()
# displayBalance(wallet)

def addfunds(wallet,amount):
    if amount<=0:
        print("amount should not be zero or negative")
        return None
    wallet["balance"]+=amount
    wallet["transection_history"].append(amount)
# wallet=initializewallet()
# amount=789
# print(addfunds(wallet,amount))


def makepayment(wallet,amount):
    if amount<0:
        print("amount should no zero")
    if wallet["balance"]<amount:
        print("insufficient balance in your wallet")
    wallet["balance"]-=amount
    wallet["transection_history"].append(amount)
# wallet=initializewallet()
# amount=100
# makepayment(wallet,amount)

def transectionhistory(wallet):
    for transection in wallet["transection_history"]:
        print(transection)
# wallet=initializewallet()
# print(transectionhistory(wallet))


def usewallet():
    print("welcome to the wallet")
    wallet=initializewallet()
    print("\n menu")
    print("1.view balance")
    print("2.add funds")
    print("3.makepayment")
    print("4.view transection history")
    print("5.exit: ")
    while True:
        choice=input("enter your choice: ")
        if choice=="1":
            displayBalance(wallet)
        if choice=="2":
            amount=float(input("add you funds: "))
            addfunds(wallet,amount)
        if choice=="3":
            amount=float(input("pay the amount: "))
            makepayment(wallet,amount)
        if choice=="4":
            transectionhistory(wallet)
        if choice=="5":
            print("you are exit: ")
usewallet()

