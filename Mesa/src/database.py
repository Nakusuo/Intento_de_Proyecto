import pyodbc
from config.db_config import Config  # Suponiendo que la configuración de tu base de datos esté en este archivo

class Database:
    @staticmethod
    def get_connection():
        try:
            # Asegúrate de usar los valores correctos para tu servidor, base de datos, usuario y contraseña
            conn_str = "Driver={ODBC Driver 17 for SQL Server};Server=your_server_name;Database=your_database_name;UID=your_user;PWD=your_password"

            conn = pyodbc.connect(conn_str)
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
