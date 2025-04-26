from dataclasses import dataclass

@dataclass
class Actividad:
    id_actividad: int
    descripcion: str
    fecha_actividad: str  # o datetime.date si usas fechas
    documento_id: int

    def __repr__(self):
        return f"<Actividad {self.id_actividad} - Documento {self.documento_id}>"
