class Bank :
    def __init__(self,accno,name,type,bal):
        self.accno =accno
        self.name =name
        self.type=type
        self.bal =bal
    def deposite(self,amount):
        self.bal=self.bal+amount
        print("Amount deosited successfuly")
        return self.bal
    def withdraw(self,amount):
        if amount >self.bal:
            print("insifficiant balance")
            return self.bal
        else:
            self.bal =self.bal -amount
            print("Amount withdraw successfuly")
            return self.bal
b = Bank(1001,"abhi","savings",3000)
damount = float(input("Enter the amount to be deposited: "))
print("Account balance:", b.deposite(damount))
wamount = float(input("Enter the amount to be withdrwn: "))
print("Account balance:", b.withdraw(wamount))
