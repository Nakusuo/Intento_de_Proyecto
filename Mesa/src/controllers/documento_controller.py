from src.database import get_connection

def obtener_documentos():
    # Obtén la conexión
    conexion = get_connection()
    
    if conexion:
        cursor = conexion.cursor()
        # Ejecuta una consulta SQL
        cursor.execute("SELECT * FROM documentos")
        documentos = cursor.fetchall()
        
        for doc in documentos:
            print(doc)
        
        # Cierra la conexión
        conexion.close()
