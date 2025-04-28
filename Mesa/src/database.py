import pyodbc
from config.db_config import Config

class Database:
    @staticmethod
    def get_connection():
        try:
            conn = pyodbc.connect(
                f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                f'SERVER={Config.DB_HOST};'
                f'DATABASE={Config.DB_NAME};'
                f'UID={Config.DB_USER};'
                f'PWD={Config.DB_PASSWORD};'
            )
            print("Conexión exitosa a la base de datos")
            return conn
        except pyodbc.Error as e:
            raise Exception(f"Error al conectar a la base de datos: {e}")

    def execute_query(self, query, params=()):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        cursor.close()
        conn.close()

    def fetch_one(self, query, params=()):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result

    def fetch_all(self, query):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results

    def execute_query_returning_id(self, query, params=()):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        inserted_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        return inserted_id
