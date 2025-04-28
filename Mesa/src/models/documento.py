from dataclasses import dataclass
from typing import Optional
from dataclasses import dataclass

@dataclass
class Documento:
    id_documento: int
    tipo_documento: str
    contenido: str
    fecha_recepcion: str  # O datetime.date
    estado: str

    def __repr__(self):
        return f"<Documento {self.id_documento} - {self.tipo_documento}>"
