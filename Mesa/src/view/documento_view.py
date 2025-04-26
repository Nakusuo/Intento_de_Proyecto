from src.controllers.documento_controller import DocumentoController

class DocumentoView:
    def __init__(self, controller: DocumentoController):
        self.controller = controller

    def menu_documentos(self):
        while True:
            print("\n--- Gestión de Documentos ---")
            print("1. Crear Documento")
            print("2. Listar Documentos")
            print("3. Buscar Documento por ID")
            print("4. Actualizar Estado de Documento")
            print("5. Eliminar Documento")
            print("6. Volver al Menú Principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.crear_documento()
            elif opcion == "2":
                self.listar_documentos()
            elif opcion == "3":
                self.buscar_documento()
            elif opcion == "4":
                self.actualizar_estado()
            elif opcion == "5":
                self.eliminar_documento()
            elif opcion == "6":
                break
            else:
                print("Opción inválida.")

    def crear_documento(self):
        tipo = input("Tipo de documento: ")
        contenido = input("Contenido del documento: ")
        fecha = input("Fecha de recepción (YYYY-MM-DD): ")
        estado = input("Estado inicial: ")
        documento = self.controller.crear_documento(tipo, contenido, fecha, estado)
        print(f"Documento creado con ID: {documento.id_documento}")

    def listar_documentos(self):
        documentos = self.controller.listar_documentos()
        for doc in documentos:
            print(f"{doc.id_documento} - {doc.tipo_documento} - {doc.estado} - {doc.fecha_recepcion}")

    def buscar_documento(self):
        id_doc = int(input("Ingrese ID del documento: "))
        doc = self.controller.obtener_documento_por_id(id_doc)
        if doc:
            print(f"Documento: {doc.tipo_documento} - {doc.estado} - {doc.fecha_recepcion}")
        else:
            print("Documento no encontrado.")

    def actualizar_estado(self):
        id_doc = int(input("ID del documento: "))
        nuevo_estado = input("Nuevo estado: ")
        self.controller.actualizar_estado_documento(id_doc, nuevo_estado)
        print("Estado actualizado.")

    def eliminar_documento(self):
        id_doc = int(input("ID del documento a eliminar: "))
        self.controller.eliminar_documento(id_doc)
        print("Documento eliminado.")
