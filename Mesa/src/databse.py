import pyodbc
from config.db_config import DB_SERVER, DB_DATABASE, DB_USER, DB_PASSWORD

def get_connection():
    try:
        # Cadena de conexión a SQL Server
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={DB_SERVER};DATABASE={DB_DATABASE};UID={DB_USER};PWD={DB_PASSWORD}'
        
        # Establecer la conexión
        conexion = pyodbc.connect(connection_string)
        return conexion
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None
