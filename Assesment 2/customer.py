from db_config import *

class Customer:

    def __init__(self, username, password):
        # Initialize customer with username, password, and initial balance of 0.0
        self.username = username
        self.password = password
        self.__balance = 0.0

    def register(self):
        # Register a new customer in the database
        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            # Insert new customer details into the customers table
            cursor.execute("INSERT INTO customers (username, password) VALUES (%s, %s)", (self.username, self.password))
            connection.commit()
            # Print success message
            print("\n\t\t\t\t\t ======================================")
            print("\t\t\t\t\t  Customer registration successful..!!")
            print("\t\t\t\t\t ======================================\n") 
        except mysql.connector.Error as err:
            # Print error message if any exception occurs
            print(f"Error: {err}")
        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()

    def login(self):
        # Log in the customer by checking credentials against the database
        connection = get_db_connection()
        cursor = connection.cursor()
        # Query to check if the customer exists with the given username and password
        cursor.execute("SELECT * FROM customers WHERE username = %s AND password = %s", (self.username, self.password))
        customer = cursor.fetchone()
        cursor.close()
        connection.close() 
        if customer:
            # Set the balance from the fetched customer record
            self.__balance = customer[3]
            # Print success message
            print("\n\t\t\t\t\t ================================")
            print("\t\t\t\t\t  Customer login successful..!!")
            print("\t\t\t\t\t ================================\n") 
            return True
        else:
            # Print error message for invalid credentials
            print("\n[ Invalid username or password..!! ]\n")
            return False

    def withdraw(self, amount):
        # Withdraw a specified amount from the customer's balance
        if amount > self.__balance:
            # Print error message if balance is insufficient
            print("\n[ Insufficient balance, Please deposit some money..!! ]\n")
        else:
            # Deduct the amount from the balance and update the database
            self.__balance -= amount
            self._update_balance()
            # Print success message
            print("\n\t\t\t\t\t Account Transaction Successful")
            print("\t\t\t\t  ---------------------------------------------")
            print(f"\t\t\t\t   Withdrawn: {amount} || Updated Balance: {self.__balance}")
            print("\t\t\t\t  ---------------------------------------------\n")

    def deposit(self, amount):
        # Deposit a specified amount to the customer's balance
        self.__balance += amount
        self._update_balance()
        # Print success message
        print("\n\t\t\t\t\t Account Transaction Successful")
        print("\t\t\t\t  ----------------------------------------------")
        print(f"\t\t\t\t   Deposited: {amount} || Updated Balance: {self.__balance}")
        print("\t\t\t\t  ----------------------------------------------\n")

    def view_balance(self):
        # View the current balance of the customer
        print("\n\t\t\t\t\t Account Transaction Successful")
        print("\t\t\t\t        ----------------------------------")
        print(f"\t\t\t\t\t     Current Balance: {self.__balance}")
        print("\t\t\t\t        ----------------------------------\n")       

    def _update_balance(self):
        # Update the balance in the database
        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            # Update the balance for the customer with the given username
            cursor.execute("UPDATE customers SET balance = %s WHERE username = %s", (self.__balance, self.username))
            connection.commit()
        except mysql.connector.Error as err:
            # Print error message if any exception occurs
            print(f"Error: {err}")
        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()
