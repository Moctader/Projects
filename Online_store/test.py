class Person:
    count_id=100
    def __init__(self, email, password) -> None:
        self.email=email
        self.password=password
        self.user_id=Person.generate_id()
        
    @classmethod
    def generate_id(self):
        id=self.count_id
        self.count_id+=1
        return id
        
    def __repr__(self) -> str:
        return (f'email: {self.email} user_id: {self.user_id}')
        

class Product:
    def __init__(self,name, price, quantity) -> None:
        self.name=name
        self.price=price
        self.quantity=quantity

class Store:
    def __init__(self) -> None:
        self.total_products={}
    def add_products(self, seller_id, products):
        print(seller_id)
        product_dict=(vars(products))
        if seller_id not in self.total_products:
            self.total_products[seller_id]=[]
            celler_info={}
            celler_info["totall_sell_amount"]=0
            celler_info["totall_amount_sell"]=0
            celler_info["toall_profit_amount"]=0
            self.total_products[seller_id].append(celler_info)
        
        self.total_products[seller_id].append(product_dict)
        
        
class Seller(Person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
        
    def add_product(self,store, product_name, product_price, product_quantity):
        product=Product(product_name, product_price, product_quantity)
        #print(vars(product))
        store.add_products(self.user_id, product)
        
        
class Customer(Person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
        
    def show_product(self, store):
        all_sellar_keys=store.total_products.keys()
        #print(all_sellar_keys)
        for seller_id in all_sellar_keys:
            print("seller_id", seller_id)
            print("==============================")
            for index in range(1, len(store.total_products[seller_id])):
                print(store.total_products[seller_id][index])
        
class Owner(Person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
        
        
store=Store()
        
seller_1=Seller("golam", 1234)
seller_2=Seller("golam@gmail.com", 1234)

seller_1.add_product(store,'i10', 2000, 12)
seller_1.add_product(store, 'i11', 3000, 12)

seller_2.add_product(store, 'i12', 4000, 12)
seller_2.add_product(store, 'i13', 5000, 12)

print(seller_1)
print(seller_2)

#print(store.total_products)
customer_1=Customer("gmail.com", 12234)
customer_1.show_product(store)
