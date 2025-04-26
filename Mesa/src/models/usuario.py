from dataclasses import dataclass

@dataclass
class Usuario:
    id_usuario: int
    nombre_usuario: str
    rol: str

    def __repr__(self):
        return f"<Usuario {self.nombre_usuario} ({self.rol})>"
