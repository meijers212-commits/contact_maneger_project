import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()


class DB_Connection:
    _connection = None

    @staticmethod
    def get_connection():

        if DB_Connection._connection and DB_Connection._connection.is_connected():
            return DB_Connection._connection

        try:
            connection = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME"),
                autocommit=True,
            )
            return connection
        except Error as e:
            print(f"Database connection error: {e}")
            return None

    @staticmethod
    def close_connection():
        if DB_Connection._connection and DB_Connection._connection.is_connected():
            DB_Connection._connection.close()
