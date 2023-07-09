class Resturants:
    def __init__(self, name, rent, menu=[]) -> None:
        self.name=name
        self.orders=[]
        self.chef=None
        self.server=None
        self.manager=None
        self.menu=menu
        self.expense=0
        self.revenu=0
        self.profit=0
        self.balance=0
        self.rent=rent
    
    def add_employee(self, employee_type, employee):
        if employee_type=='chef':
            self.chef=employee
        elif employee_type=='server':
            self.server=employee
        elif employee_type=='manager':
            self.manager=employee
    
    def add_order(self, order):
        self.orders.append(order)
        
    def recive_payment(self, order, amount, customer):
       # print(amount, order.bill)
        if amount>order.bill:
            self.revenu +=order.bill
            self.balance +=order.bill
            customer.bill_due=0
            return amount-order.bill
        else:
            print('Not have enough money')
            
    def pay_expense(self, amount, description):
        if amount<self.balance:
            self.expense+=amount
            self.balance -=amount
            print(f'Expense {amount} for {description}')
            
        else:
            print(f'Not have enough money')
            
    def pay_salary(self, employee):
        print(f'paying salary for {employee.name} salary: {employee.salary}')
        if employee.salary<self.balance:
            self.balance-=employee.salary
            self.expense+=employee.salary
            employee.recive_salary()
            
            
    def show_employee(self):
        if self.chef is not None:
            print(f'chef: {self.chef.name} wtih salary: {self.chef.salary}')
        if self.server is not None:
            print(f'server: {self.server.name} wtih salary: {self.server.salary}')
        if self.manager is not None:
            print(f'manager: {self.manager.name} wtih salary: {self.manager.salary}')