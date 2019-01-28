print("Today's Menu Options!")
menu = ["Cheese Burger", "Double Cheeseburger", 
        "BBQ Pulled Chicken Sandwich", "BBQ Burger","BBQ Bologna Sandwich"]
price = [4.29,6.29,4.29,5.49,3.99]

print("1 - Cheese Burger - 4.29\n2 - Double CheeseBurger - 6.29\n3 - BBQ Pulled Chicken Sandwich - 4.29\n4 - BBQ Burger - 5.49\n5 - BBQ Bologna Sandwich - 3.99")

userChoice = int(input("What would you like to order?")) - 1
print("You have selected: " + str(menu[userChoice]) + " $" + str(price[userChoice]))


