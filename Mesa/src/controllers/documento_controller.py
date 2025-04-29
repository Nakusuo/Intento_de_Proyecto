from src.models.documento import Documento
from src.database import Database

class DocumentoController:
    def __init__(self, db: Database):
        self.db = db

    def obtener_tipos_documento(self):
        query = "SELECT id_tipo, nombre FROM TipoDocumento"
        try:
            resultados = self.db.fetch_all(query)
            return {nombre: id_tipo for id_tipo, nombre in resultados}
        except Exception as e:
            print(f"Error al obtener tipos de documento: {e}")
            return {}

    def obtener_lista_personal(self):
        query = "SELECT id_personal, nombre FROM Personal"
        try:
            resultados = self.db.fetch_all(query)
            return {nombre: id_personal for id_personal, nombre in resultados}
        except Exception as e:
            print(f"Error al obtener personal: {e}")
            return {}

    def obtener_documentos(self):
        query = """
            SELECT d.id_documento, td.nombre AS tipo_documento, d.contenido, d.fecha_recepcion, d.estado, p.nombre AS personal
            FROM documentos d
            JOIN TipoDocumento td ON d.tipo_documento_id = td.id_tipo
            LEFT JOIN Personal p ON d.personal_id = p.id_personal
        """
        try:
            resultados = self.db.fetch_all(query)
            documentos = []
            for row in resultados:
                documentos.append({
                    "id_documento": row[0],
                    "tipo_documento": row[1],
                    "contenido": row[2],
                    "fecha_recepcion": row[3],
                    "estado": row[4],
                    "personal": row[5] or "Sin asignar",
                })
            return documentos
        except Exception as e:
            print(f"Error al obtener documentos: {e}")
            return []

    def obtener_personal_con_tareas(self):
        query = """
            SELECT 
                p.nombre, 
                p.area, 
                COUNT(CASE WHEN d.estado = 'Pendiente' THEN 1 END) AS documentos_pendientes,
                COUNT(CASE WHEN d.estado = 'Realizado' THEN 1 END) AS documentos_realizados
            FROM Personal p
            LEFT JOIN documentos d ON p.id_personal = d.personal_id
            GROUP BY p.nombre, p.area
        """
        try:
            resultados = self.db.fetch_all(query)
            personal = []
            for row in resultados:
                personal.append({
                    "nombre": row[0],
                    "area": row[1],
                    "pendientes": row[2],
                    "realizados": row[3]
                })
            return personal
        except Exception as e:
            print(f"Error al obtener tareas del personal: {e}")
            return []

    def obtener_pendientes_por_personal(self, nombre_personal):
        query = """
            SELECT d.id_documento, td.nombre AS tipo_documento, d.contenido, d.fecha_recepcion
            FROM documentos d
            JOIN TipoDocumento td ON d.tipo_documento_id = td.id_tipo
            JOIN Personal p ON d.personal_id = p.id_personal
            WHERE p.nombre = ? AND d.estado = 'Pendiente'
        """
        try:
            return self.db.fetch_all(query, (nombre_personal,))
        except Exception as e:
            print(f"Error al obtener pendientes de {nombre_personal}: {e}")
            return []
