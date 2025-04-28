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
        OUTPUT INSERTED.id_usuario
        VALUES (?, ?)
        """
        params = (nombre_usuario, rol)
        nuevo_id = self.db.execute_query_returning_id(query, params)
        nuevo_usuario.id_usuario = nuevo_id
        return nuevo_usuario

    def obtener_usuario_por_id(self, id_usuario):
        query = "SELECT * FROM usuarios WHERE id_usuario = ?"
        result = self.db.fetch_one(query, (id_usuario,))
        if result is not None:
            if len(result) == 3:  # id_usuario, nombre_usuario, rol
                return Usuario(*result)
            else:
                print("Error: La cantidad de columnas en el resultado no coincide con los parámetros de Usuario.")
        return None

    def listar_usuarios(self):
        query = "SELECT * FROM usuarios"
        results = self.db.fetch_all(query)
        return [Usuario(*row) for row in results]

    def actualizar_rol_usuario(self, id_usuario, nuevo_rol):
        query = "UPDATE usuarios SET rol = ? WHERE id_usuario = ?"
        self.db.execute_query(query, (nuevo_rol, id_usuario))

    def eliminar_usuario(self, id_usuario):
        query = "DELETE FROM usuarios WHERE id_usuario = ?"
        self.db.execute_query(query, (id_usuario,))
