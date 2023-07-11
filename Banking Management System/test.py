class User:
    def __init__(self, username, password) -> None:
        self.username=username
        self.password=password
        
class Company:
    def __init__(self,name) -> None:
        self.name=name
    user_list=[]
    
    def create_account(self):
        name=input("Enter your username: ")
        password=input("Enter your password: ")
        self.new_user=User(name, password)
        self.user_list.append(vars(self.new_user))
        
    def get_user(self):
        return self.user_list


class Account:
    def __init__(self, account_name, password) -> None:
        self.account_name=account_name
        self.password=password
        self.balance=0
        self.loan_limit=100000
        self.transaction_history=[]
        self.totall_loan=0
    
    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
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
                print("Insufficient Balance")
                
    # def transection_history(self):
    #     print(f'Transection history for account: {self.account_name}')
    #     for transections in self.transaction_history:
    #         print(transections)
    
    # def __repr__(self) -> str:
    #     for transections in self.transaction_history:
    #         print(transections)
    #     return ''
    
    def take_loan(self):
        if self.balance*2<=self.loan_limit:
            loan_amount=self.balance*2
            self.balance +=loan_amount
            self.totall_loan+=loan_amount
            print(f'loan granted: {loan_amount} for the account {self.account_name}')
                        
            
    def check_balance(self):
        print(f'Account Name: {self.account_name} Balance: {self.balance}')
        
    def totall_loan_amount(self):
        print(f'totall loan: {self.totall_loan}')