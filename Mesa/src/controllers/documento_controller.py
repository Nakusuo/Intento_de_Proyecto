from src.models.documento import Documento
from src.database import Database  # supondremos que tienes una clase Database en database.py

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
        # Lógica para guardar en la base de datos
        query = """
        INSERT INTO documentos (tipo_documento, contenido, fecha_recepcion, estado)
        VALUES (%s, %s, %s, %s)
        RETURNING id_documento
        """
        params = (tipo_documento, contenido, fecha_recepcion, estado)
        nuevo_id = self.db.execute_query_returning_id(query, params)
        nuevo_documento.id_documento = nuevo_id
        return nuevo_documento

    def obtener_documento_por_id(self, id_documento):
        query = "SELECT * FROM documentos WHERE id_documento = %s"
        result = self.db.fetch_one(query, (id_documento,))
        if result:
            return Documento(*result)
        return None

    def listar_documentos(self):
        query = "SELECT * FROM documentos"
        results = self.db.fetch_all(query)
        return [Documento(*row) for row in results]

    def actualizar_estado_documento(self, id_documento, nuevo_estado):
        query = "UPDATE documentos SET estado = %s WHERE id_documento = %s"
        self.db.execute_query(query, (nuevo_estado, id_documento))

    def eliminar_documento(self, id_documento):
        query = "DELETE FROM documentos WHERE id_documento = %s"
        self.db.execute_query(query, (id_documento,))
