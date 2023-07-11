from Banking_system import*
def main():
    while True:
        company=Company('bank')
        account=Account('name', 'password')
        print("1. Create an account\n2. login to your account\n3. exit")
        user_input=int(input("Enter your choice: "))
        if user_input==3:
            break
        elif user_input==1:
            company.create_account()
            
        elif user_input==2:
            name=input("Enter your username: ")
            password=input("Enter your password: ")
            
            flag=0
            is_admin=False
            if name=="admin" and password=="123":
                is_admin=True
            if is_admin==False:
                for user in company.get_user():
                    if user['username']==name and user['password']==password:
        
                        print("welcome to the Bank account")
                        account= Account(name,password)
                        account.deposit(1000)
                        account.withdraw(200)
                        account.check_balance()
                        account.take_loan()
                        
                        
                
            else:
                while True:
                    
                    print("hello admin")
                    print("1. Create an account\n2. exit\n3. Totall_balace\n4. Toall loan amount\n5. feature control")
                    
                    user_input=int(input("Enter your choice: "))
                    if user_input==2:
                            break
                    elif user_input==1:
                        company.create_account()  
                    elif user_input==3:
                        account.check_balance()
                    elif user_input==4:
                        account.totall_loan_amount()
                        
                            
                
        
if __name__=='__main__':
    main()