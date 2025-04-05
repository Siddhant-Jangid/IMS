import mysql.connector

def remove_item():
    conn = mysql.connector.connect(
    host = 'hostname',
    user = 'username',
    password = 'your_password',
    database = 'database_name'
    )

    cursor = conn.cursor()

    id = input("Enter id= \n")
    query = "DELETE FROM table_name WHERE id = %s"
    data = (id,)
    cursor.execute(query,data)
    conn.commit()
    cursor.close()
    conn.close()


    
