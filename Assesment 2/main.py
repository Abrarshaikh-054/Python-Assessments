from banker import *
from customer import *

def main():
    # Display a welcome message
    print("\n\t\t\t\t     ====================================")
    print("\t\t\t\t      Welcome to the Banking Application")
    print("\t\t\t\t     ====================================\n")

    while True:
        # Display the main menu options
        print("\t\t\t\t\t ||======= MAIN MENU =======||\n")
        print("\t\t\t\t\t  1. Banker   (press 1)")
        print("\t\t\t\t\t  2. Customer (press 2)")
        print("\t\t\t\t\t  3. Exit     (press 3)")

        try: 
            # Get the user's choice
            rl_ch = int(input("\n> Enter your choice : "))
        except ValueError:
            # Handle invalid input for menu choice
            print("\n[ Invalid input, Please try again..!! ]\n")
            continue

        if rl_ch == 1:
            # Go to the banker menu
            banker_menu()
        elif rl_ch == 2:
            # Go to the customer menu
            customer_menu()
        elif rl_ch == 3:
            # Exit the application
            print("\nThank you for using the Banking Application :)\n")
            break
        else:
            # Handle invalid menu choice
            print("\n[ Invalid choice, Please try again..!! ]\n")

def banker_menu():
    while True:
        # Display the banker menu options
        print("\n\t\t\t\t\t ||====== BANKER MENU ======||\n")
        print("\t\t\t\t\t  1. Register")
        print("\t\t\t\t\t  2. Login")
        print("\t\t\t\t\t  3. Back to Main Menu")

        try:
            # Get the user's choice
            ch = int(input("\n> Enter your choice : "))
        except ValueError:
            # Handle invalid input for menu choice
            print("\n[ Invalid input, Please try again..!! ]\n")
            continue  

        if ch == 1:
            # Register a new banker
            username = input("\n> Enter username: ")
            password = input("> Enter password: ")
            banker = Banker(username, password)
            banker.register()
        elif ch == 2:
            # Banker login
            username = input("\n> Enter username: ")
            password = input("> Enter password: ")
            banker = Banker(username, password)

            if banker.login():
                # Display the banker operations menu after successful login
                while True:
                    print("\n\t\t\t\t\t    ||====== BANKER MENU ======||\n")
                    print("\t\t\t\t\t     1. View all Customers")
                    print("\t\t\t\t\t     2. Update Customer")
                    print("\t\t\t\t\t     3. Delete Customer")
                    print("\t\t\t\t\t     4. Logout\n")
                    
                    try:
                        # Get the banker's choice of operation
                        br_ch = int(input("> Enter your choice : "))
                    except ValueError:
                        # Handle invalid input for operation choice
                        print("\n[ Invalid input, Please try again..!! ]\n")
                        continue

                    if br_ch == 1:
                        # View all customers
                        banker.view_all_customers()
                    elif br_ch == 2:
                        # Update a customer
                        while True:
                            try:    
                                customer_id = int(input("\n> Enter customer ID to update: "))
                            except ValueError:
                                # Handle invalid customer ID input
                                print("\n[ Invalid input, Please enter a valid ID number..!! ]") 
                                continue

                            if banker.id_exists(customer_id):
                                banker.update_customer(customer_id)
                                break
                            else:
                                continue
                    elif br_ch == 3: 
                        # Delete a customer
                        while True:
                            try:
                                customer_id = int(input("\n> Enter customer ID to delete : "))
                                
                                if banker.id_exists(customer_id):
                                    while True:
                                        con = input("\n> Do you really want to delete this customer? (y/n): ").lower() 

                                        if con == 'y':
                                            banker.delete_customer(customer_id)
                                            break
                                        elif con == 'n':
                                            print("\n[ Customer deletion cancelled..!! ]\n")
                                            break
                                        else:
                                            # Handle invalid confirmation input
                                            print("\n[ Invalid choice, please enter 'y' or 'n' ]")  
                                    
                                    break  # Exit the outer loop after handling confirmation
                                else:
                                    continue
                            except ValueError:
                                # Handle invalid customer ID input
                                print("\n[ Invalid input, Please enter a valid ID number..!! ]") 
                    elif br_ch == 4:
                        # Logout
                        break
                    else:
                        # Handle invalid operation choice
                        print("\n[ Invalid choice, Please try again..!! ]\n")
        elif ch == 3:
            # Back to the main menu
            break
        else:
            # Handle invalid menu choice
            print("\n[ Invalid choice, Please try again..!! ]\n")

def customer_menu():
    while True:
        # Display the customer menu options
        print("\t\t\t\t\t ||====== CUSTOMER MENU ======||\n")
        print("\t\t\t\t\t  1. Register")
        print("\t\t\t\t\t  2. Login")
        print("\t\t\t\t\t  3. Back to Main Menu")

        try:
            # Get the user's choice
            ch = int(input("\n> Enter your choice : "))
        except ValueError:
            # Handle invalid input for menu choice
            print("\n[ Invalid input, Please try again..!! ]\n")
            continue

        if ch == 1:
            # Register a new customer
            username = input("\n> Enter username: ")
            password = input("> Enter password: ")
            customer = Customer(username, password)
            customer.register()
        elif ch == 2:
            # Customer login
            username = input("\n> Enter username: ")
            password = input("> Enter password: ")
            customer = Customer(username, password)

            if customer.login():
                # Display the customer operations menu after successful login
                while True:
                    print("\t\t\t\t\t ||====== CUSTOMER MENU ======||\n")
                    print("\t\t\t\t\t  1. Withdraw Amount")
                    print("\t\t\t\t\t  2. Deposit Amount")
                    print("\t\t\t\t\t  3. View Balance")
                    print("\t\t\t\t\t  4. Logout")

                    try:
                        # Get the customer's choice of operation
                        cr_ch = int(input("\n> Enter your choice : "))

                        if cr_ch == 1:
                            # Withdraw amount
                            while True:
                                try:        
                                    amount = float(input("\n> Enter amount to withdraw: "))
                                    customer.withdraw(amount)
                                    break
                                except ValueError:
                                    # Handle invalid amount input
                                    print("\n[ Invalid input, Please enter a valid amount..!! ]")
                        elif cr_ch == 2:
                            # Deposit amount
                            while True:
                                try:
                                    amount = float(input("\n> Enter amount to deposit: "))
                                    customer.deposit(amount)
                                    break
                                except ValueError:
                                    # Handle invalid amount input
                                    print("\n[ Invalid input, Please enter a valid amount..!! ]")
                        elif cr_ch == 3:
                            # View balance
                            customer.view_balance()
                        elif cr_ch == 4:
                            # Logout
                            break
                        else:
                            # Handle invalid operation choice
                            print("\n[ Invalid choice, Please try again..!! ]\n")
                    except ValueError:
                        # Handle invalid input for operation choice
                        print("\n[ Invalid input, Please try again..!! ]\n")
                        continue
        elif ch == 3:
            # Back to the main menu
            break
        else:
            # Handle invalid menu choice
            print("\n[ Invalid choice, Please try again..!! ]\n")

main()
