import mysql.connector

def remove_item():
    conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '@trishule_1793',
    database = 'inventory'
    )

    cursor = conn.cursor()

    id = input("Enter id= \n")
    query = "DELETE FROM details WHERE id = %s"
    data = (id,)
    cursor.execute(query,data)
    conn.commit()
    cursor.close()
    conn.close()


    