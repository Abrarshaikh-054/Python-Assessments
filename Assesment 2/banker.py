from db_config import *

class Banker:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register(self):
        # Establish a connection to the database
        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            # Insert new banker details into the bankers table
            cursor.execute("INSERT INTO bankers (username, password) VALUES (%s, %s)", (self.username, self.password))
            connection.commit()

            # Print success message
            print("\n\t\t\t\t     =====================================")
            print("\t\t\t\t      Banker Registration Successful..!!")
            print("\t\t\t\t     =====================================")    
        except mysql.connector.Error as err:
            # Print error message if any exception occurs
            print(f"Error: {err}")
        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()

    def login(self):
        # Establish a connection to the database
        connection = get_db_connection()
        cursor = connection.cursor()
        # Query to check if the banker exists with the given username and password
        cursor.execute("SELECT * FROM bankers WHERE username = %s AND password = %s", (self.username, self.password))
        banker = cursor.fetchone()
        cursor.close()
        connection.close()
        if banker:
            # Print success message if login is successful
            print("\n\t\t\t\t\t   ==============================")
            print("\t\t\t\t\t    Banker login successful..!!")
            print("\t\t\t\t\t   ==============================")
            return True
        else:
            # Print error message if login fails
            print("\n[ Invalid username or password..!! ]\n")
            return False

    def view_all_customers(self):
        # Establish a connection to the database
        connection = get_db_connection()
        cursor = connection.cursor()
        # Query to fetch all customer details
        cursor.execute("SELECT * FROM customers")
        customers = cursor.fetchall()
        cursor.close()
        connection.close()
        # Print the details of all customers
        self.print_customers(customers)

    def print_customers(self, customers):
        if not customers:
            # Print message if no customers are found
            print("\n[ No customers found ]\n") 
            return

        # Print headers for customer details
        print(f"\n\t\t\t\t {'ID':<5} {'Username':<20} {'Password':<20} {'Balance':<10}")
        print("\t\t\t\t=========================================================")

        # Print each customer's details
        for customer in customers:
            print(f"\n\t\t\t\t {customer[0]:<5} {customer[1]:<20} {customer[2]:<20} {customer[3]:<10}")

        print("\n\t\t\t\t=========================================================")

    def id_exists(self, customer_id):
        # Establish a connection to the database
        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            # Query to check if the customer exists with the given ID
            cursor.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))
            customer = cursor.fetchone()
            if customer:
                return True
            else:
                # Print message if the ID does not exist
                print(f"\n[ ID number {customer_id} does not exist, Please enter a valid ID number..!! ]")
                return False
        except mysql.connector.Error as err:
            # Print error message if any exception occurs
            print(f"Error: {err}")

    def update_customer(self, customer_id):
        # Establish a connection to the database
        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            # Get new username and password for the customer
            username = input("\n> Enter new username: ")
            password = input("> Enter new password: ")
            # Update the customer details in the database
            cursor.execute("UPDATE customers SET username = %s, password = %s WHERE id = %s", (username, password, customer_id))
            connection.commit()
            # Print success message
            print("\n\t\t\t\t\t  ====================================")
            print("\t\t\t\t\t   Customer Updated Successfully...!!")
            print("\t\t\t\t\t  ====================================")
            cursor.close()
            connection.close()
            return True
        except mysql.connector.Error as err:
            # Print error message if any exception occurs
            print(f"Error: {err}")

    def delete_customer(self, customer_id):
        # Establish a connection to the database
        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            # Delete the customer from the database
            cursor.execute("DELETE FROM customers WHERE id = %s", (customer_id,))
            connection.commit()
            # Print success message
            print("\n\t\t\t\t\t  ====================================")
            print("\t\t\t\t\t   Customer Deleted Successfully...!!")
            print("\t\t\t\t\t  ====================================")
            cursor.close()
            connection.close()
            return True
        except mysql.connector.Error as err:
            # Print error message if any exception occurs
            print(f"Error: {err}")
