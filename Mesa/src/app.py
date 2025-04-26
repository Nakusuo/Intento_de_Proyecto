# src/app.py

from src.database import DatabaseConfig

def main():
    # Prueba de conexión a la base de datos
    conn = DatabaseConfig.get_connection()
    if conn:
        print("Conexión exitosa a SQL Server.")
        # Puedes probar con una consulta
        cursor = conn.cursor()
        cursor.execute("SELECT @@VERSION;")  # Consulta para verificar la versión de SQL Server
        sql_version = cursor.fetchone()
        print("Versión de SQL Server:", sql_version)
        conn.close()
    else:
        print("No se pudo conectar a SQL Server.")

if __name__ == "__main__":
    main()
