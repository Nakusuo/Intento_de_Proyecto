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
