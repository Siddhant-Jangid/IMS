import mysql.connector

def add_item():
    conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '@trishule_1793',
    database = 'inventory'
    )

    cursor = conn.cursor()

    id = input("Enter item id= \n")
    name = input("Enter item name= \n")
    price = input("Enter item's price= \n")
    amount = input("Enter the amount of item= \n")

    query = "INSERT INTO details (ID,name,price,amount) VALUES (%s,%s,%s,%s)"
    data = (id,name,price,amount)
    cursor.execute(query,data)
    conn.commit()
    cursor.close()
    conn.close()

