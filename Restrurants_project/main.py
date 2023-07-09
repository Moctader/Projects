from Menu import*
from Resturants import*
from User import*
from Order import*
def main():
    menu=Menu()
    pizza_1=Pizza('sotki pizza', 2000, 'large', ['sotki', 'oniion'])
    menu.add_menu_item('pizza', pizza_1)
    pizza_2=Pizza('alur vorta pizza', 3000, 'medium',['alu', 'onion', 'oil'])
    menu.add_menu_item('pizza', pizza_2)
    pizza_3=Pizza('Dal pizza', 4000, 'small', ['dal', 'alu'])
    menu.add_menu_item('pizza', pizza_3)
    
    # add Burger 
    burger_1=Burger('naga',2000,'meat', ['chiclen, oil'])
    menu.add_menu_item('burger', burger_1)
    burger_2=Burger('hot',3000, 'beef',['beef', 'potato'])
    menu.add_menu_item('burger', burger_2)
    burger_3=Burger('lamp',1000, 'lamp', ['lamp','potato_mash'])
    menu.add_menu_item('burger', burger_3)
    
    #Add drinks
    drink_1=Drinks('cocacola',100, True)
    menu.add_menu_item('drinks', drink_1)
    
    drink_2=Drinks('pepsi', 110, True)
    menu.add_menu_item('drinks', drink_2)
    
    drink_3=Drinks('cofee',50, False)
    menu.add_menu_item('drinks', drink_3)
    
    #show menu
    #menu.show_menu()
    
    #Resturant
    resturant=Resturants('name of the resturant',2000, menu)  
    
    #add employess  
    manager=Manager('boss',345,'@gmail.com','valuka',2000, '01 2023', 'core')
    resturant.add_employee('manager', manager)
    chef=Chef('chef',455, '@gmail.com', 'naogaon', 2000, '01 3030', 'core','everything')
    resturant.add_employee('chef', chef)
    server=Server('choto', 45, '@', 'jdk',2000, '01 2023', 'core')
    resturant.add_employee('server', server)
    
    #Show employee
    resturant.show_employee()
    
    #customer
    customer_1=Customer('skib khan', 4567, '@gmail.com','nowapara', 2000)
    order_1=Order(customer_1, [pizza_3, drink_3])
    customer_1.pay_for_prder(order_1)
    resturant.add_order(order_1)
    
    #customer 1 paying for order1 
    resturant.recive_payment(order_1,9000, customer_1)
    print('Revenue and bonus after first customer: ',resturant.revenu, resturant.balance)


    #customer2
    customer_2=Customer('skib khan', 4567, '@gmail.com','nowapara', 2000)
    order_2=Order(customer_2, [pizza_3, drink_3])
    customer_2.pay_for_prder(order_2)
    resturant.add_order(order_2)

    #customer 2 paying for order1 
    resturant.recive_payment(order_1,9000, customer_1)
    print('Revenue and bonus after second customer: ',resturant.revenu, resturant.balance)
    
    #Pay rent
    resturant.pay_expense(resturant.rent, 'Rent')
    print('after rent', resturant.revenu, resturant.balance, resturant.expense)
    
    resturant.pay_salary(chef)
    print('after rent', resturant.revenu, resturant.balance, resturant.expense)

#call the main function
if __name__== '__main__':
    main()

