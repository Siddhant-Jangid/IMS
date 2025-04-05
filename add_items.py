import mysql.connector

def add_item():
    conn = mysql.connector.connect(
    host = 'hostname',
    user = 'username',
    password = 'your_password',
    database = 'database_name'
    )

    cursor = conn.cursor()

    id = input("Enter item id= \n")
    name = input("Enter item name= \n")
    price = input("Enter item's price= \n")
    amount = input("Enter the amount of item= \n")

    query = "INSERT INTO table_name (ID,name,price,amount) VALUES (%s,%s,%s,%s)"
    data = (id,name,price,amount)
    cursor.execute(query,data)
    conn.commit()
    cursor.close()
    conn.close()

