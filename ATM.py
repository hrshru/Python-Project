class account:
    def __init__(self,balance):
        self.balance=balance
        return
    def withdraw(self,amount):
        print("trying to withdraw:",amount)
        print("avalable Bal:",self.balance)
        if amount<=self.balance:
            print("collect:",amount)
            self.balance=self.balance-amount
        else:
            print("low balance:")
            return
class Bank:
    def main():
        amount=int(input("Enter initial balance:"))
        acc=account(amount)
        print("Balance is:",acc.balance)
        amount=int(input("Enter the Withdraw amount:"))
        acc.withdraw(amount)
        print("final bal is:",acc.balance)
        return
Bank.main()    
