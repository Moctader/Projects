from banking_system import*
def main():
    while True:
        company=Account_name('name',1223, 'customer')
        
        print("1. Create an account\n2. login to your account\n3. exit")
        user_input=int(input("Enter your choice: "))
        if user_input==3:
            break
        elif user_input==1:
            company.create_account()
            
        elif user_input==2:
            name=input("Enter your username: ")
            password=input("Enter your password: ")
            
           
            is_admin=False
            if name=="admin" and password=="123":
                is_admin=True
            if is_admin==False:
                flag=0
                for user in company.get_user():
                    if user['username']==name and user['password']==password:
                        
                        print("welcome to the Bank account")
                        company.deposit(int(input("Enter your deposit amount: ")))
                        company.withdraw(int(input("Enter your withdrawal amount: ")))
                        company.check_balance()
                        company.take_loan()
                        company.transection_history()
                        
                        
                
            else:
                while True:
                    
                    company1=Admin('name',1223)
                    print("hello admin")
                    print("1. Create an account\n2. exit\n3. Totall_balace\n4. Toall loan amount\n5. feature control")
                    
                    user_input=int(input("Enter your choice: "))
                    if user_input==2:
                            break
                    elif user_input==1:
                        company.create_account()  
                    elif user_input==3:
                        company1.check_bank_balance()
                    elif user_input==4:
                        company1.check_loan_amount()
                    elif user_input==5:
                        company1.loan_feature_function(True)
                        
                            
                
        
if __name__=='__main__':
    main()