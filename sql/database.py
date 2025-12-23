import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv


def get_connection():
    load_dotenv(dotenv_path="../sql/.env")
    try:
        connection = mysql.connector.connect(
            host=os.getenv("HOST"),            
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DATABASE")
        )
        return connection
    except Error as e:
        print(f"Database connection error: {e}")
        return None
