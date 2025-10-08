'''
class student:
    def __init__(self,name,roll_number,mark):
        self.name=name
        self.roll_number=roll_number
        self.mark=mark
    def calculate_grade(self):
        print("name:",self.name)
        print("roll_number:",self.roll_number)
        print("mark:",self.mark)
        if(self.mark>=90):
            print("grade:O")
        elif(self.mark>=80):
            print("grade:A")
        elif(self.mark>=70):
            print("grade:B")
        elif(self.mark>=60):
            print("grade:C")
        elif(self.mark>=50):
            print("grade:D")
        elif(self.mark<35):
            print("grade:fail")
        
obj=student("raghul",85,80)
obj.calculate_grade()
print("========")
obj1=student("prajith",81,70)
obj1.calculate_grade()
print("========")
obj2=student("aaaa",67,60)
obj2.calculate_grade()
print("========")
obj3=student("raghul",65,34)
obj3.calculate_grade()
print("========")
'''

#wrong
'''class bank_account:
    def __init__(self,account_holder,balance,Account_balance):
        self.account_holder=account_holder
        self.balance=balance
        self.Account_balance=Account_balance
    def deposit(self):
        print("account_holder:",self.account_holder)
        deposit_amount=int(input("deposit amount"))
        Account_balance=deposit_amount+self.balance
        print(Account_balance)
    def withdraw(self):
        withdraw_amount=int(input("withdraw_amount"))
        print(self.Account_balance = -withdraw_amount)
obj=bank_account("prajith",500,"")
obj.deposit()
obj.withdraw()'''

        
'''class bank_account:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self):
        deposit_amount=int(input("enter deposit amount:"))
        self.balance += deposit_amount
        print("account_balance:",self.balance)
    def withdraw(self):
        withdraw_amount=int(input("enter withdraw_amount:"))
        self.balance-=withdraw_amount
    def get_balance(self):
        print("current balance:",self.balance)
obj=bank_account("raghul",500)
obj.deposit()
obj.withdraw()
obj.get_balance()'''


























        
        

























  
