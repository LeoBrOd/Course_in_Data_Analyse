import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

HOSTNAME = os.getenv('DB_HOSTNAME')
USERNAME = os.getenv('DB_USERNAME')
PASSWORD = os.getenv('DB_PASSWORD')
DATABASE = os.getenv('DB_DATABASE')

connection = psycopg2.connect(
    host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)


class DbConnection:
    @staticmethod
    def execute_change(query, values):
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        cursor.close()

    @staticmethod
    def execute_select(query, values=None):
        cursor = connection.cursor()
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results
