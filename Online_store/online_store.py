class Person:
    id_counter=100
    def __init__(self, email, password) -> None:
        self.email=email
        self.password=password
        self.user_id=Person.generate_id()
        
    @classmethod
    def generate_id(self):
        id=self.id_counter
        self.id_counter+=1
        return id
        
    
    def __repr__(self) -> str:
        return(f'email: {self.email} passwprd: {self.user_id}')
    
class Product:
    def __init__(self, name, price, Quantity) -> None:
        self.name=name
        self.price=price
        self.Quantity=Quantity
        
    def __repr__(self) -> str:
        return (f'product_name: {self.name}|| product_price: {self.price}|| product_Quantity: {self.Quantity}')
    
    
    
class Store:
    def __init__(self) -> None:
       self.total_products={}
    
    def add_product(self, seller_id, product):
        # print(seller_id)
        # print(vars(product))
        product_dic=vars(product)
        if seller_id  not in self.total_products:
            self.total_products[seller_id]=[]
            seller_info={}
            seller_info["totall_sell_product"]=0
            seller_info["totall_sell_amount"]=0
            seller_info["totall_profit_amount"]=0
            self.total_products[seller_id].append(seller_info)
            
        self.total_products[seller_id].append(product_dic)
            
       

    

class Sellar(Person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
        
    def add_product(self,store, product_name, product_price, product_Quantity):
        product=Product(product_name, product_price, product_Quantity)
        store.add_product(self.user_id, product)
        
        
        
class Owner(Person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password) 
        
class Customer(Person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
        
    def show_products(self,store):
        #print(store.total_products)
        all_seller_keys=store.total_products.keys()
        #print(all_seller_keys)
        for seller_id in all_seller_keys:
            print("seller_id:", seller_id)
            print("============================")
            # for product in store.total_products[seller_id]:
            #     print("name", product["name"], "price:",product["price"], "Quantity: ", product["Quantity"])
            for index in range(1, len(store.total_products[seller_id])):
                print(store.total_products[seller_id][index])

store=Store()

Sellar_1=Sellar("sellar1@gmail.com", 1234)
Sellar_2=Sellar("sellar2@gmail.com", 1235)
Sellar_3=Sellar("sellar2@gmail.com", 1235)

Sellar_1.add_product(store,'i10', 20, 10)
Sellar_1.add_product(store, 'i10', 20, 10)

Sellar_2.add_product(store, 'i11', 20, 11)
Sellar_2.add_product(store, 'i11', 20, 11)

Sellar_3.add_product(store,'i12', 20, 12)
Sellar_3.add_product(store, 'i12', 20, 12)

#print(store.total_products)
customer_1=Customer('df@gmail.com', 12345)
customer_1.show_products(store)
