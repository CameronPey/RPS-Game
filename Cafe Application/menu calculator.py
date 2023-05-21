# Defining the options, prices, name of the store, and the starting total
def cafeShopCalculation():
    version = 1.03
    total = 0
    topping = 0.15
    customer_accounts = {}
    cafe_name = 'Summer Dining Cafe!'
    sizes = {'s': 'small', 'm': 'medium', 'l': 'large'}
    prices = {'s': 3.65, 'm': 4.85, 'l': 6.25}
    drink_prices = {'frappe': 2.25, 'black coffee': 1.75, 'latte': .85, 'refresher': .65}

    def get_input(prompt):
        while True:
            try:
                return input(prompt).lower()
            except KeyboardInterrupt:
                exit()

    def handle_version():
        print(version)

    def handle_prices():
        for size, price in prices.items():
            print(f'{sizes[size].capitalize()}: {price}')
    
    def handle_signup():
        customer_number = get_input('Enter your account number')
        if customer_number in customer_accounts:
            print('Account already exists. Please proceed with your order.')
        else:
            customer_name = get_input('Enter your name: ')
            customer_accounts[customer_number] = {'name': customer_name, 'points': 0}
            print('Account created successfully. Proceed with your order')

    def add_drink_to_order(drink_size):
        nonlocal total
        total += prices[drink_size]
        drink_type = get_input('What type of drink would you like to order? ')

        if drink_type == 'frappe':
            add_frappe(drink_size)
        elif drink_type == 'black coffee':
            add_black_coffee(drink_size)
        elif drink_type == 'latte':
            add_latte(drink_size)
        elif drink_type == 'refresher':
            add_refresher(drink_size)
        else:
            print('Invalid drink type. Please choose from the menu.')

    def add_frappe(drink_size):
        whipped_cream = get_input('Would you like any whipped cream? (yes or no) ')
        if whipped_cream == 'yes':
            print(f'A Frappe with whipped cream was added to the order ({sizes[drink_size]}).')
            nonlocal total
            total += topping

    def add_black_coffee(drink_size):
        nonlocal total
        total += drink_prices['black coffee']
        cream_sugar = get_input('Would you like any cream or sugar? (yes or no) ')
        if cream_sugar == 'yes':
            handle_cream_sugar()

    def handle_cream_sugar():
        options = get_input('Would you like cream or sugar? ')
        quantity = float(get_input('How many would you like? '))
        if options == 'cream':
            cream_cost = quantity * 0.08
            nonlocal total
            total += cream_cost
            print(f'A Black coffee with {quantity} creams has been added to the order!')
        elif options == 'sugar':
            sugar_cost = quantity * 0.12
            total += sugar_cost
            print(f'A Black coffee with {quantity} sugars has been added to the order!')
        else:
            print('Invalid option. Please choose either cream or sugar.')

    def add_latte(drink_size):
        option = get_input('Would you like it iced or hot? ')
        if option == 'iced':
            nonlocal total
            total += drink_prices['latte'] + drink_prices[drink_size]
            print(f'An iced latte has been added to the order ({sizes[drink_size]}).')
        elif option == 'hot':
            total += drink_prices['latte'] + drink_prices[drink_size]
            print(f'A hot latte has been added to the order ({sizes[drink_size]}).')
        else:
            print('Invalid option. Please choose either iced or hot.')

    def add_refresher(drink_size):
        option = get_input('What type of refresher? Strawberry, Cherry, or Regular? ')
        if option.lower() in ['strawberry', 'cherry', 'regular']:
            nonlocal total
            total += drink_prices['refresher']
            print(f'A {option.capitalize()} refresher has been added to the order ({sizes[drink_size]}).')
        else:
            print('Invalid option. Please choose from the menu.')

    def handle_order():
        customer_number = get_input('Enter your account number (or leave empty if not applicable): ')
        if customer_number in customer_accounts:
            print(f'Hello, {customer_accounts[customer_number]["name"]}!')
        elif customer_number != '':
            print('Account not found. Please sign up or enter a valid account number.')
        order_complete = False
        while not order_complete:
            drink_size = get_input('What size would you like? (s, m, l) ')
            if drink_size in sizes:
                add_drink_to_order(drink_size)
                add_another_drink = get_input('Would you like to add another drink? (yes or no) ')
                if add_another_drink == 'no':
                    order_complete = True
            else:
                print('Invalid drink size. Please choose from the menu.')

    def handle_payment():
        payment_method = get_input('How would you like to pay? (cash or card) ')
        if payment_method == 'cash':
            cash_received = float(get_input('Enter the amount of cash received: $'))
            if cash_received < total:
                print('Insufficient payment. Please provide enough cash.')
                handle_payment()
            else:
                change = cash_received - total
                print(f'Total: ${total:.2f}')
                print(f'Cash received: ${cash_received:.2f}')
                print(f'Change: ${change:.2f}')
        elif payment_method == 'card':
            customer_number = get_input('Enter your account number: ')
            if customer_number in customer_accounts:
                customer_accounts[customer_number]['points'] += int(total)
                print('Points updated successfully.')
            else:
                print('Account not found. Points not updated.')
            print(f'Total: ${total:.2f}')
            print('Payment successfully processed with a card.')
        else:
            print('Invalid payment method. Please choose either cash or card.')

    # Main menu
    while True:
        print(f'Welcome to {cafe_name}!')
        print('1. Calculate prices')
        print('2. Order drinks')
        print('3. Make payment')
        print('4. Software Version')
        print('5. Rewards Sign Up')
        print('6. Exit')

        option = get_input('Select an option: ')
        if option == '1':
            handle_prices()
        elif option == '2':
            handle_order()
        elif option == '3':
            handle_payment()
        elif option == '4':
            handle_version()
        elif option == '5':
            handle_signup()
        elif option == '6':
            print('Thank you for visiting. Goodbye!')
            break
        else:
            print('Invalid option. Please choose from the menu.')

cafeShopCalculation()