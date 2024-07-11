import bcrypt
import psycopg2
from psycopg2 import sql

def register_admin(username, password):
    try:
        # Connect to your postgres DB
        conn = psycopg2.connect(
            dbname='mydatabase',
            user='postgres',
            password='123456',
            host='localhost',
            port=5432
        )
        
        # Create a cursor object
        cursor = conn.cursor()
        
        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        # Create the SQL statement
        insert_query = sql.SQL("INSERT INTO admins (username, password) VALUES (%s, %s)")
        
        # Execute the SQL statement
        cursor.execute(insert_query, (username, hashed_password))
        
        # Commit the transaction
        conn.commit()
        
        # Close the cursor and connection
        cursor.close()
        conn.close()
        
        print("Admin registered successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Usage
username = 'admin'
password = '123456'
register_admin(username, password)
