def menu():
    print("Menu".center(43,"-"))
    print(f"|{'Item'.upper():^20}|{'Price'.upper():^20}|")
    print("-"*43)
    print(f"|{'Burger':^20}|{'₹129':^20}|")
    print(f"|{'Fries':^20}|{'₹99':^20}|")
    print(f"|{'Coke':^20}|{'₹79':^20}|")
    print(f"|{'Piri-Piri':^20}|{'₹39':^20}|")
    print(f"|{'Salad':^20}|{'₹159':^20}|")
    print("-"*43)
    print("\n\n")
menu()
def order(Customer_name,*item,**Specifications):
    pass
    """"This is used to create a order with flexible options and gives you the total."""
    print(f"---Order for {Customer_name}---".upper())
    total=0
    item_prices={'burger':129,'fries':99,'coke':79,"piri piri":39,'salad':159}

    for items in item:
        total+= item_prices.get(items.lower(),50)
        print(f"- {items.title():<16}:₹{item_prices[items.lower()]}")


    if Specifications.get("Extra_cheese"):
        pass
        print(f"+ Extra Cheese    :₹50")
        total+=50
    if Specifications.get("Extra_jalapeno"):
        print(f"+ Extra Jalapeno  :₹50")
        total+=50


    delivery_type=Specifications.get("delivery","Pickup")
    tip=Specifications.get("tip",0)

    if delivery_type=="delivery":
        print("+ Delivery Charges:₹50")
        total+=50
    if tip!=0:
        print(f"+ {'Tip':<16}:₹{tip}")
        total+=tip
    print("-"*20)
    print("")
    
    print(f"Subtotal: ₹{total:.2f}")
    print(f"GST(5%): ₹{total+total*5/100}")
    print("Payment Method: Cash")
    print(f"Delivery type: {delivery_type}")
order("Ayden","Burger","coke","fries","Salad",Extra_cheese=2,Extra_jalapeno=2,delivery="delivery",tip=20)

