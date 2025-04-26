class Usuario:
    def __init__(self, id_usuario, nombre_usuario, rol):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.rol = rol

    def __repr__(self):
        return f"<Usuario {self.nombre_usuario} ({self.rol})>"
