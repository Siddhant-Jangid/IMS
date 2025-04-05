from tabulate import tabulate

import mysql.connector

def view_inventory():
    try:
        # Establish connection to MySQL database
        connection = mysql.connector.connect(
            host="hostname",
            user="username",
            password="your_password",
            database="database_name"
        )

        cursor = connection.cursor()
        
        query = "SELECT * FROM table_name"
        cursor.execute(query)
        
        records = cursor.fetchall()
        
        if records:
            headers = ["ID", "Product Name", "Price", "Quantity"]
            
            print("\nCurrent Inventory:")
            print(tabulate(records, headers=headers, tablefmt="grid"))
        else:
            print("\nNo items found in inventory.")

    except mysql.connector.Error as error:
        print(f"Failed to view inventory: {error}")
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


