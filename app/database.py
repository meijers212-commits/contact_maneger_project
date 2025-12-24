import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():

    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),            
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            autocommit=True
        )
        return connection
    except Error as e:
        print(f"Database connection error: {e}")
        return None
