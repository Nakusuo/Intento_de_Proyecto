from src.database import DatabaseConfig

def main():
    # Obtener la conexión a la base de datos
    conn = DatabaseConfig.get_connection()
    
    if conn:
        # Puedes realizar consultas con conn aquí, por ejemplo:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tu_tabla")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        conn.close()  # No olvides cerrar la conexión después de usarla

if __name__ == "__main__":
    main()
