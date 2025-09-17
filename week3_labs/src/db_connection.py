import mysql.connector
from mysql.connector import Error
def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="divinogwapo12",
            database="fletapp"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None
    
if __name__ == "__main__":
    conn = connect_db()
    if conn:
        print("✅ Connection successful!")
        print("Server info:", conn.get_server_info())
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("Connected to database:", record)
        cursor.close()
        conn.close()
    else:
        print("❌ Connection failed!")
