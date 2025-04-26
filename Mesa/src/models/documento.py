from dataclasses import dataclass
from typing import Optional

@dataclass
class Documento:
    id_documento: int
    tipo_documento: str
    contenido: str
    fecha_recepcion: str  # O datetime.date
    estado: str
    actividad_relacionada: Optional[int] = None

    def __repr__(self):
        return f"<Documento {self.id_documento} - {self.tipo_documento}>"
