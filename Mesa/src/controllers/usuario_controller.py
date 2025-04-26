from src.models.usuario import Usuario
from src.database import Database

class UsuarioController:
    def __init__(self, db: Database):
        self.db = db

    def crear_usuario(self, nombre_usuario, rol):
        nuevo_usuario = Usuario(
            id_usuario=None,
            nombre_usuario=nombre_usuario,
            rol=rol
        )
        query = """
        INSERT INTO usuarios (nombre_usuario, rol)
        VALUES (%s, %s)
        RETURNING id_usuario
        """
        params = (nombre_usuario, rol)
        nuevo_id = self.db.execute_query_returning_id(query, params)
        nuevo_usuario.id_usuario = nuevo_id
        return nuevo_usuario

    def obtener_usuario_por_id(self, id_usuario):
        query = "SELECT * FROM usuarios WHERE id_usuario = %s"
        result = self.db.fetch_one(query, (id_usuario,))
        if result:
            return Usuario(*result)
        return None

    def listar_usuarios(self):
        query = "SELECT * FROM usuarios"
        results = self.db.fetch_all(query)
        return [Usuario(*row) for row in results]

    def actualizar_rol_usuario(self, id_usuario, nuevo_rol):
        query = "UPDATE usuarios SET rol = %s WHERE id_usuario = %s"
        self.db.execute_query(query, (nuevo_rol, id_usuario))

    def eliminar_usuario(self, id_usuario):
        query = "DELETE FROM usuarios WHERE id_usuario = %s"
        self.db.execute_query(query, (id_usuario,))
