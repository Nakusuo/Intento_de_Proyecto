import pyodbc
from config.db_config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

# Función para establecer la conexión
def get_connection():
    try:
        # Construcción de la cadena de conexión
        conexion = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'  # Usa el driver adecuado para tu versión
            f'SERVER={DB_HOST};'
            f'DATABASE={DB_NAME};'
            f'UID={DB_USER};'
            f'PWD={DB_PASSWORD}'
        )
        print("Conexión exitosa")
        return conexion
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
