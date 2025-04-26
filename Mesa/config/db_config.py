import psycopg2
from config.config import Config

class DatabaseConfig:
    """Clase para manejar la conexión a la base de datos."""

    @staticmethod
    def get_connection():
        """Devuelve una conexión a la base de datos usando la configuración."""
        conn = psycopg2.connect(Config.get_db_connection())
        return conn
