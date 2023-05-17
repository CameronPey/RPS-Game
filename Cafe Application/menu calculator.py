# This is a simple calculating program for a small coffee cafe


# Defining what the options, pricem version, name of the store, and the starting total is
def cafeShopCalculation():
    version = 1.02
    total = 0
    topping = .15
    cafe_name = 'Summer Dining Cafe!'
    medium = .86
    large = .79
    sizes = {'s':'small','m':'medium','l':'large'}
    while True:
        try:
            customer = input('Welcome to the ' + cafe_name + '. What size of drink would you like to start with today? (s, m, l) ')
            customer = customer.lower()
            if customer in ['v', 'version']:
                print(version)
            elif customer in ['p', 'price', 'prices']:
                print(medium)
                print(large)
            elif customer in sizes:
                if customer == 's':
                    total += 3.65
                    drinks = input('What type of drink would you like to order? ')
                    drinks = drinks.lower()
                    if drinks == 'frappe':
                        while True:
                            toppings = input('Would you like any whipped cream? ')
                            toppings = toppings.lower()
                            if toppings == 'yes':
                                print('A Frappe with whipped cream was added to the order. ')
                                total += topping
                                break
                            elif toppings == 'no':
                                print('A Frappe with no whipped cream was added to the order. ')
                                break
                            else:
                                print('Please make sure to select yes or no for whipped cream')
                    elif drinks == 'black coffee':
                        total += 1.75
                        toppings = input('Would you like any cream or sugar? (y or n)')
                        toppings = toppings.lower()
                        if toppings == 'y':
                            while True:
                                options = input('Would you like cream or sugar? ')
                                options = options.lower()
                                if options == 'cream':
                                    quantity = input('How many creams would you like to have? ')
                                    cream_cost = float(quantity) * .08
                                    total += cream_cost
                                    print('A Black coffee with ',quantity, 'creams have been added to the order! ')
                                    break
                                elif options == 'sugar':
                                    quantity = input('How many sugars would you like to have? ')
                                    sugar_cost = float(quantity) * .12
                                    total += sugar_cost
                                    print('A Black coffee with ',quantity, 'sugars have been added to the order! ')
                                    break
                                else:
                                    print('Please make sure to select Cream or sugar')
                        elif toppings == 'n':
                            print('A Black coffee with no cream or sugar has been added to the order! ')
                    elif drinks == 'latte':
                        while True:
                            option = input('Would you like it iced or hot? ')
                            option = option.lower()
                            if option == 'iced':
                                total += 3.36
                                print('A iced latte has been added to the order. ')
                                break
                            elif option == 'hot':
                                total += 2.72
                                print('A hot latte has been added to the order. ')
                                break
                            else:
                                print('Please make sure to either say Iced or Hot')
                    elif drinks == 'refresher':
                        while True:
                            total += 3.28
                            option = input('What type of refresher? Strawberry, Cherry, or Regular?')
                            option = option.lower()
                            if option == 'strawberry':
                                print('A small strawberry refresher has been added to the order. ')
                                break
                            elif option == 'cherry':
                                print('A small cherry refresher has been added to the order. ')
                                break
                            elif option == 'regular':
                                print('A small regular refresher has been added to the order. ')
                                break
                            else:
                                print('Please make sure to pick either strawberry, cherry, or regular ')
                elif customer == 'm':
                    total += 3.65
                    total += medium
                    drinks = input('What type of drink would you like to order? ')
                    drinks = drinks.lower()
                    if drinks == 'frappe':
                        while True:
                            toppings = input('Would you like any whipped cream?')
                            toppings = toppings.lower()
                            if toppings == 'yes':
                                print('A Frappe with whipped cream was added to the order. ')
                                total += topping
                                break
                            if toppings == 'no':
                                print('A Frappe with no whipped cream was added to the order. ')
                                break
                            else:
                                print('Please make sure to select yes or no for whipped cream')
                    elif drinks == 'black coffee':
                        total += 1.75
                        total += medium
                        while True:
                            toppings = input('Would you like any cream or sugar? (y or n)')
                            toppings = toppings.lower()
                            if toppings == 'y':
                                options = input('Would you like cream or sugar? ')
                                options = options.lower()
                                if options == 'cream':
                                    quantity = input('How many creams would you like to have? ')
                                    cream_cost = float(quantity) * .08
                                    total += cream_cost
                                    print('A Black coffee with ',quantity, 'creams have been added to the order! ')
                                    break
                                elif options == 'sugar':
                                    quantity = input('How many sugars would you like to have? ')
                                    sugar_cost = float(quantity) * .12
                                    total += sugar_cost
                                    print('A Black coffee with ',quantity, 'sugars have been added to the order! ')
                                    break
                                else:
                                    print('Please make sure to select Cream or sugar')
                            elif toppings == 'n':
                                print('A Black coffee with no cream or sugar has been added to the order! ')
                    elif drinks == 'latte':
                        while True:
                            option = input('Would you like it iced or hot? ')
                            option = option.lower()
                            if option == 'iced':
                                total += 3.36
                                total += medium
                                print('A iced latte has been added to the order. ')
                                break
                            elif option == 'hot':
                                total += 2.72
                                total += medium
                                print('A hot latte has been added to the order. ')
                                break
                    elif drinks == 'refresher':
                        total += 3.28
                        total += medium
                        while True:
                            option = input('What type of refresher? Strawberry, Cherry, or Regular?')
                            option = option.lower()
                            if option == 'strawberry':
                                print('A small strawberry refresher has been added to the order. ')
                                break
                            elif option == 'cherry':
                                print('A small cherry refresher has been added to the order. ')
                                break
                            elif option == 'regular':
                                print('A small regular refresher has been added to the order. ')
                                break
                            else:
                                print('Please make sure to pick either strawberry, cherry, or regular ') 
                elif customer == 'l':
                    total += 3.65
                    total += large
                    while True:
                        drinks = input('What type of drink would you like to order? ')
                        drinks = drinks.lower()
                        if drinks == 'frappe':
                            toppings = input('Would you like any whipped cream?')
                            toppings = toppings.lower()
                            if toppings == 'yes':
                                print('A Frappe with whipped cream was added to the order. ')
                                total += topping
                                break
                            if toppings == 'no':
                                print('A Frappe with no whipped cream was added to the order. ')
                                break
                            else:
                                print('Please make sure to select yes or no for whipped cream')
                elif drinks == 'black coffee':
                        total += 1.75
                        total += large
                        while True:
                            toppings = input('Would you like any cream or sugar? (y or n)')
                            toppings = toppings.lower()
                            if toppings == 'y':
                                options = input('Would you like cream or sugar? ')
                                options = options.lower()
                                if options == 'cream':
                                    quantity = input('How many creams would you like to have? ')
                                    cream_cost = float(quantity) * .08
                                    total += cream_cost
                                    print('A Black coffee with ',quantity, 'creams have been added to the order! ')
                                elif options == 'sugar':
                                    quantity = input('How many sugars would you like to have? ')
                                    sugar_cost = float(quantity) * .12
                                    total += sugar_cost
                                    print('A Black coffee with ',quantity, 'sugars have been added to the order! ')
                                else:
                                    print('Please make sure to select Cream or sugar')
                            elif toppings == 'n':
                                print('A Black coffee with no cream or sugar has been added to the order! ')
                elif drinks == 'latte':
                    while True:
                        option = input('Would you like it iced or hot? ')
                        option = option.lower()
                        if option == 'iced':
                            total += 3.36
                            total += large
                            print('A iced latte has been added to the order. ')
                            break
                        elif option == 'hot':
                            total += 2.72
                            total += large
                            print('A hot latte has been added to the order. ')
                            break
                elif drinks == 'refresher':
                        total += 3.28
                        total += large
                        while True:
                            option = input('What type of refresher? Strawberry, Cherry, or Regular?')
                            option = option.lower()
                            if option == 'strawberry':
                                print('A small strawberry refresher has been added to the order. ')
                                break
                            elif option == 'cherry':
                                print('A small cherry refresher has been added to the order. ')
                                break
                            elif option == 'regular':
                                print('A small regular refresher has been added to the order. ')
                                break
                            else:
                                print('Please make sure to pick either strawberry, cherry, or regular ') 

            # Once the customer is done ordering, they would say 'Done' and it would ask how they would like to pay. Currently only having Cash or Card as the options/
            elif customer == 'done':
                print(total)
                while True:
                    payment_method = input('How would you like to pay today? Cash or Card? ')
                    if payment_method == 'card':
                        cardTotal = total + .80
                        print('The total today would be ', cardTotal )
                        break
                    elif payment_method == 'cash':
                        print('The total today would be ', total)
                        break
                    else:
                        print('Please make sure to select either Cash or Card!')
            else:
                print('Make sure to select an item from the menu! ')
        except KeyboardInterrupt:
            exit()
cafeShopCalculation()    