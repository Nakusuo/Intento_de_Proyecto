class Actividad:
    def __init__(self, id_actividad, descripcion, fecha_actividad, documento_id):
        self.id_actividad = id_actividad
        self.descripcion = descripcion
        self.fecha_actividad = fecha_actividad
        self.documento_id = documento_id

    def __repr__(self):
        return f"<Actividad {self.id_actividad} - Documento {self.documento_id}>"
