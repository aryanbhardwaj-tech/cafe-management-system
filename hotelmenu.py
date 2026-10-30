menu = {
    "pizza":120,
    "burger":60,
    "pasta":70,
    "french fries":50,
    "cold coffee":60,
}

print(menu)

print("Welcome to Elevate Cafe")
print("Pizza: Rs120\nBurger: Rs60\nPasta: Rs70\nFrench Fries: Rs50\nCold Cofee: Rs60")

order_total = 0
item_1 = input("Enter Name of item You want to order = ")
if item_1 in menu:
    order_total += menu[item_1] 
    print(f"Your item{item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet!")
    another_order = input("Do you want to add another item? (Yes/No)")
    if another_order == "Yes":
        item_2 = input("Enter the name of second item = ")
        if item_2 in menu:
           order_total += menu[item_2]
           print(f"item {item_2} has been added to order")
        else:
            print(f"Ordered item {item_2} is not available!")
            print(f"The total amount of items to pay is {order_total}")
