import mysql.connector

def search_item_by_id():
    try:
        connection = mysql.connector.connect(
            host="hostname",
            user="username",
            password="your_password",
            database="database_name"
        )
        
        cursor = connection.cursor()
        
        item_id = input("Enter Item ID to search: ")
        
        query = "SELECT * FROM table_name WHERE id = %s"
        cursor.execute(query, (item_id,))
        
        result = cursor.fetchone()
        
        if result:
            print("\nItem Found:")
            print(f"ID: {result[0]}")
            print(f"Name: {result[1]}")
            print(f"Quantity: {result[3]}")
            print(f"Price: {result[2]}Rs/-\n\n")
        else:
            print("No item found with that ID.\n\n")

    except mysql.connector.Error as error:
        print(f"Error: {error}")
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def search_item_by_name():
    try:
        connection = mysql.connector.connect(
            host="hostname",
            user="username",
            password="your_password",
            database="database_name"
        )
        
        cursor = connection.cursor()
        
        item_name = input("Enter Item name to search: ")
        
        query = "SELECT * FROM table_name WHERE name = %s"
        cursor.execute(query, (item_name,))
        
        result = cursor.fetchone()
        
        if result:
            print("\nItem Found:")
            print(f"ID: {result[0]}")
            print(f"Name: {result[1]}")
            print(f"Quantity: {result[3]}")
            print(f"Price: {result[2]}Rs/-\n\n")
        else:
            print("No item found with that name.\n\n")

    except mysql.connector.Error as error:
        print(f"Error: {error}")
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
