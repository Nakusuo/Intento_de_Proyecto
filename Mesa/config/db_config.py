import pyodbc

class Config:
    DB_HOST = 'DESKTOP-TJ16A60'  # Dirección del servidor SQL
    DB_NAME = 'NakusuBD'  # Nombre de la base de datos
    DB_USER = 'sa'        # Usuario de conexión
    DB_PASSWORD = 'admin123'  # Contraseña del usuario

# Función para probar la conexión
def test_connection():
    try:
        conn = pyodbc.connect(
            f'DRIVER={{Driver for SQL Server}};'
            f'SERVER={Config.DB_HOST};'
            f'DATABASE={Config.DB_NAME};'
            f'UID={Config.DB_USER};'
            f'PWD={Config.DB_PASSWORD}'
        )
        print("Conexión exitosa")
        conn.close()
    except Exception as e:
        print(f"Error de conexión: {e}")

if __name__ == '__main__':
    test_connection()
