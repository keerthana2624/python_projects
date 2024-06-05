def initializeWallet():
    wallet={"balance=0","transaction_history=[]"}
    return wallet
# print(initializeWallet())


def displaybalance(wallet):
    balance=wallet["balance"]
    print(f"current balance:{wallet}")
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

