import pyodbc
from config.db_config import Config

def crear_tablas():
    conn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={Config.DB_HOST};'
        f'DATABASE={Config.DB_NAME};'
        f'UID={Config.DB_USER};'
        f'PWD={Config.DB_PASSWORD};'
    )
    cursor = conn.cursor()
    
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
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    crear_tablas()
