class User:
    def __init__(self, username, password) -> None:
        self.username=username
        self.password=password
        

    
class Account_name(User):
    Totall_money=0
    Total_loan=0
    loan_feature=True
    transaction_history=[]
    
    def __init__(self, username, password, account_name) -> None:
        super().__init__(username, password)
        self.account_name=account_name
        #self.password=password
        self.balance=0
        self.loan_limit=100000
        #self.transaction_history=[]
        self.totall_loan=0
    
    user_list=[]
    
    def create_account(self):
        name=input("Enter your username: ")
        password=input("Enter your password: ")
        self.new_user=User(name, password)
        self.user_list.append(vars(self.new_user))
        
        
    def get_user(self):
        return self.user_list

    
    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
            Account_name.Totall_money +=amount
            self.transaction_history.append(f'Deposited: {amount}')
            print(f'Deposited {amount} into account {self.account_name}')
            self.check_balance()
        else: 
            print("Insufficient Balance")
            
    def withdraw(self, amount):
        if amount>0:
            if amount<=self.balance:
                self.balance -=amount
                self.transaction_history.append(f'withdraw: {amount}')
                print(f'Withdraw {amount} from account name: {self.account_name}')
                self.check_balance()
            else:
                print("bank is bankrupt")
                
    def transection_history(self):
        #print(f'Transection history for account: {self.account_name}')
        for transections in Account_name.transaction_history:
            print(transections)
    
    # def __repr__(self) -> str:
    #     for transections in self.transaction_history:
    #         print(transections)
    #     return ''
    
    def take_loan(self):
        if Account_name.loan_feature:
            if self.balance*2<=self.loan_limit:
                loan_amount=self.balance*2
                self.balance +=loan_amount
                #self.totall_loan+=loan_amount
                Account_name.Total_loan+=loan_amount
                print(f'loan granted: {loan_amount} for the account {self.account_name}')
                
    def check_balance(self):
        print(f'Account Name: {self.account_name} Balance: {self.balance}')
                        
            
  
        
        
class Admin(User):
    def __init__(self, username, password) -> None:
        super().__init__(username, password)

        
    # def totall_loan_amount(self):
    #     print(f'totall loan: {self.totall_loan}')
    
    def check_bank_balance(self):
        print(f'Totall bank balance: {Account_name.Totall_money}')
        
    def check_loan_amount(self):
        print(f'Totall amount of bank loan: {Account_name.Total_loan}')
    
    def loan_feature_function(self, enable):
        Account_name.loan_feature=enable
        if enable:
            status="enabled"
        else:
            status="disabled"
        print(f'The loan feature has been: {status}')
        
