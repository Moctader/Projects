from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, phone , email, address) -> None:
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address
        
class Customer(User):
    def __init__(self,  name, phone , email, address, money) -> None:
        self.wallet=money
        self.__order=None
        self.bill_due=0
        super().__init__( name, phone , email, address)
        
    @property
    def order(self):
        return self.__order
    
    def order(self, order):
        self.__order=order
        
    def place_order(self, order):
        self.order=order
        self.bill_due+=order.bill
        print(f'{self.name} order name {order.items}')
        
    def eat_food(self, order):
        print(f'{self.name} order items {order.items}')
        
    def pay_for_prder(self, amount):
        pass
    
    def give_tips(self, tips_amount):
        pass
    
    def write_star(self, stars):
        pass
    
class Employee(User):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        self.salary=salary
        self.due=salary
        self.starting_date=starting_date
        self.department=department
        super().__init__(name, phone, email, address)
    
    def recive_salary(self):
        self.due=0
        
        
class Chef(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department,cooking_item) -> None:
        self.cooking_item=cooking_item
        super().__init__(name, phone, email, address, salary, starting_date, department)

class Server(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        self.tips_earning=0
        super().__init__(name, phone, email, address, salary, starting_date, department)
        
    def take_order(self, order):
        pass
    
    def transfer_order(self, order):
        pass
    
    def serve_food(self, order):
        pass
    
    def recive_tips(self, amount):
        self.tips_earning+=amount
        
        
class Manager(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)
        
    
    
    
    