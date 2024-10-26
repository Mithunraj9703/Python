class Account:
    def __init__(self,bal,no):
        self.balance=bal
        self.account_no=no

    def debit(self,amount):
        self.balance-=amount
        print("Ammount is debited ",amount)
        print("Total balance is ",self.balance1())

    def credit(self,amount):
        self.balance+=amount
        print("Amount is credited ",amount)
        print("Total balance is ",self.balance1())

    def balance1(self):
        # print("Now remaining balance ",self.balance)
        return self.balance

acc1=Account(10000,12345)
print("Account balance is ",acc1.balance)
print("Accout number is ",acc1.account_no)
acc1.debit(1000)
acc1.credit(2000)
# acc1.balance1()
