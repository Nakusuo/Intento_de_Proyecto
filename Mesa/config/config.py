# src/database.py

import pyodbc
from config.db_config import Config

class DatabaseConfig:
    """Clase para manejar la conexión a la base de datos SQL Server."""

    @staticmethod
    def get_connection():
        """Devuelve una conexión a SQL Server usando la configuración."""
        try:
            conn = pyodbc.connect(
                f'DRIVER={{ODBC Driver 17 for SQL Server}};'  # Especifica el driver ODBC
                f'SERVER={Config.DB_HOST};'
                f'DATABASE={Config.DB_NAME};'
                f'UID={Config.DB_USER};'
                f'PWD={Config.DB_PASSWORD};'
            )
            return conn
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None
PASSWORD = 'TuContraseñaSegura'  # Contraseña de la base de datos
