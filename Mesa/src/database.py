import pyodbc
from config.db_config import Config

class Database:
    @staticmethod
    def get_connection():
        try:
            # Cadena de conexión para Microsoft SQL Server usando pyodbc
            conn = pyodbc.connect(
                f'DRIVER={{ODBC Driver 17 for SQL Server}};'  # Especifica el driver ODBC
                f'SERVER={Config.DB_HOST};'  # Dirección del servidor
                f'DATABASE={Config.DB_NAME};'  # Nombre de la base de datos
                f'UID={Config.DB_USER};'  # Usuario
                f'PWD={Config.DB_PASSWORD};'  # Contraseña
            )
            print("Conexión exitosa a la base de datos")
            return conn
        except pyodbc.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None
