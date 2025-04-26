import pyodbc
from config.db_config import Config

def crear_tablas():
    try:
        # Establecer la conexión con la base de datos
        conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={Config.DB_HOST};'
            f'DATABASE={Config.DB_NAME};'
            f'UID={Config.DB_USER};'
            f'PWD={Config.DB_PASSWORD};'
        )
        cursor = conn.cursor()

        # Crear la tabla 'documentos' si no existe
        cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'documentos')
        BEGIN
            CREATE TABLE documentos (
                id_documento INT PRIMARY KEY IDENTITY,
                tipo_documento NVARCHAR(100),
                contenido NVARCHAR(MAX),
                fecha_recepcion DATE,
                estado NVARCHAR(50)
            )
        END
        """)
        
        # Confirmar los cambios
        conn.commit()

    except pyodbc.Error as e:
        print(f"Error en la base de datos: {e}")
    finally:
        # Asegurarse de cerrar la conexión y el cursor
        cursor.close()
        conn.close()

if __name__ == "__main__":
    crear_tablas()
