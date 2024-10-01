class Account:
    def __init__(self, bal, acc_no):
        self.balance = bal
        self.account_no = acc_no
    
    def cedit(self,amount):
        self.balance += amount
        print(f'{amount} is been credited')
        print(f'Total Amount is {self.balance}')
    
    def dedit(self,amount):
        self.balance -= amount
        print(f'{amount} is been debited')
        print(f'Total Amount is {self.balance}')
user1 = Account(10000, 1234)
user1.cedit(500)
user1.dedit(1000)
        