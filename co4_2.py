class bank:
    def __init__(self,accno,accname,acctyp,accbal):
        self.accountnumber=accno
        self.accountname=accname
        self.accounttype=acctyp
        self.accountbalance=accbal
        
        
    def display(self):
        
        print("\n--- Bank Account Details ---")
        print("Account Number:", self.accountnumber)
        print("Account Holder:", self.accountname)
        print("Account Type:", self.accounttype)
        print("Balance:", self.accountbalance)

    
    def deposit(self, amount):
        if amount > 0:
            self.accountbalance += amount
            print("Amount deposited successfully.")
            print("Current Balance:", self.accountbalance)
        else:
            print("Invalid deposit amount!")
    
    1
    def withdraw(self,amount):
        if amount<=0:
            print("Invalid amount!")
        elif amount<=self.accountbalance:
            self.accountbalance-=amount
            print("Amount successfully withdrawn!")
            print("Current Balance ",self.accountbalance)
        else:
            print("Insuffcient balance ")
            
            
acc1 = bank(301, "Sherin", "Salary", 7999)
acc2 = bank(307, "Blessen ", "savings", 8777)


acc1.display()
acc2.display()


acc1.deposit(100)
acc2.deposit(20000)


acc1.display()
acc2.display()

acc1.withdraw(100)
acc2.withdraw(500)

acc1.display()
acc2.display()
