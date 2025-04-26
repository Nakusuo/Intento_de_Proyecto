class Documento:
    def __init__(self, id_documento, tipo_documento, contenido, fecha_recepcion, estado, actividad_relacionada=None):
        self.id_documento = id_documento
        self.tipo_documento = tipo_documento
        self.contenido = contenido
        self.fecha_recepcion = fecha_recepcion
        self.estado = estado
        self.actividad_relacionada = actividad_relacionada

    def __repr__(self):
        return f"<Documento {self.id_documento} - {self.tipo_documento}>"
