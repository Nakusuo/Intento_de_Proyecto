from src.models.documento import Documento
from src.database import Database

class DocumentoController:
    def __init__(self, db: Database):
        self.db = db

    def crear_documento(self, tipo_documento, contenido, fecha_recepcion, estado):
        nuevo_documento = Documento(
            id_documento=None,  # Al crear es None, la base de datos lo asignará
            tipo_documento=tipo_documento,
            contenido=contenido,
            fecha_recepcion=fecha_recepcion,
            estado=estado
        )
        query = """
        INSERT INTO documentos (tipo_documento, contenido, fecha_recepcion, estado)
        OUTPUT INSERTED.id_documento  -- Obtiene el ID del nuevo documento insertado
        VALUES (?, ?, ?, ?)
        """
        params = (tipo_documento, contenido, fecha_recepcion, estado)
        try:
            nuevo_id = self.db.execute_query_returning_id(query, params)
            nuevo_documento.id_documento = nuevo_id
        except Exception as e:
            print(f"Error al crear documento: {e}")
        return nuevo_documento

    def obtener_documento_por_id(self, id_documento):
        query = "SELECT * FROM documentos WHERE id_documento = ?"
        try:
            result = self.db.fetch_one(query, (id_documento,))
            if result is not None:
                return Documento(*result)
        except Exception as e:
            print(f"Error al obtener documento: {e}")
        return None

    def listar_documentos(self):
        query = "SELECT * FROM documentos"
        try:
            results = self.db.fetch_all(query)
            return [Documento(*row) for row in results]
        except Exception as e:
            print(f"Error al listar documentos: {e}")
        return []

    def actualizar_estado_documento(self, id_documento, nuevo_estado):
        query = "UPDATE documentos SET estado = ? WHERE id_documento = ?"
        try:
            self.db.execute_query(query, (nuevo_estado, id_documento))
        except Exception as e:
            print(f"Error al actualizar estado del documento: {e}")

    def eliminar_documento(self, id_documento):
        query = "DELETE FROM documentos WHERE id_documento = ?"
        try:
            self.db.execute_query(query, (id_documento,))
        except Exception as e:
            print(f"Error al eliminar documento: {e}")
