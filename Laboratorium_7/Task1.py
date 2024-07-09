class Bank_Account:
    def x(self, amount_bank_account, operation):
        try:
            # operation 1
            if operation == '1':
                if amount_bank_account <= 0: raise ValueError("Deposit amount must be positive")
                self.Balance = self.Balance + amount_bank_account
            #     operation 2
            if operation == '2':
                if amount_bank_account <= 0: raise TypeError("Withdrawal amount must be positive")



                if amount_bank_account > self.Balance: raise ValueError("Not enough funds")
                self.Balance = self.Balance - amount_bank_account
        except:
            pass
        
        

    def __init__(self, Balance):
        # balance
        self.Balance = Balance
    def getBalance(self):
        return self.Balance

b = Bank_Account(10)
b.x(10, '2')
