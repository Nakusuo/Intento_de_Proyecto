import tkinter as tk
from tkinter import messagebox
from src.controllers.documento_controller import DocumentoController

class DocumentoView:
    def __init__(self, controller: DocumentoController):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title("Gestión de Documentos")

    def menu_documentos(self):
        # Limpia la ventana y muestra las opciones de menú
        for widget in self.window.winfo_children():
            widget.destroy()

        label = tk.Label(self.window, text="--- Gestión de Documentos ---", font=("Arial", 14))
        label.pack(pady=10)

        botones = [
            ("Crear Documento", self.crear_documento),
            ("Listar Documentos", self.listar_documentos),
            ("Buscar Documento por ID", self.buscar_documento),
            ("Actualizar Estado de Documento", self.actualizar_estado),
            ("Eliminar Documento", self.eliminar_documento),
            ("Volver al Menú Principal", self.window.quit),
        ]

        for texto, comando in botones:
            button = tk.Button(self.window, text=texto, command=comando, width=30, height=2)
            button.pack(pady=5)

    def crear_documento(self):
        # Ventana para crear documento
        self._limpiar_ventana()

        tk.Label(self.window, text="Tipo de documento:").pack(pady=5)
        tipo = tk.Entry(self.window)
        tipo.pack(pady=5)

        tk.Label(self.window, text="Contenido del documento:").pack(pady=5)
        contenido = tk.Entry(self.window)
        contenido.pack(pady=5)

        tk.Label(self.window, text="Fecha de recepción (YYYY-MM-DD):").pack(pady=5)
        fecha = tk.Entry(self.window)
        fecha.pack(pady=5)

        tk.Label(self.window, text="Estado inicial:").pack(pady=5)
        estado = tk.Entry(self.window)
        estado.pack(pady=5)

        def crear():
            documento = self.controller.crear_documento(tipo.get(), contenido.get(), fecha.get(), estado.get())
            messagebox.showinfo("Información", f"Documento creado con ID: {documento.id_documento}")
            self.menu_documentos()

        button = tk.Button(self.window, text="Crear Documento", command=crear)
        button.pack(pady=20)

    def listar_documentos(self):
        # Ventana para listar documentos
        self._limpiar_ventana()
        documentos = self.controller.listar_documentos()

        for doc in documentos:
            tk.Label(self.window, text=f"{doc.id_documento} - {doc.tipo_documento} - {doc.estado} - {doc.fecha_recepcion}").pack()

        button = tk.Button(self.window, text="Volver", command=self.menu_documentos)
        button.pack(pady=10)

    def buscar_documento(self):
        # Ventana para buscar documento por ID
        self._limpiar_ventana()

        tk.Label(self.window, text="Ingrese ID del documento:").pack(pady=5)
        id_doc = tk.Entry(self.window)
        id_doc.pack(pady=5)

        def buscar():
            doc = self.controller.obtener_documento_por_id(int(id_doc.get()))
            if doc:
                messagebox.showinfo("Documento encontrado", f"Documento: {doc.tipo_documento} - {doc.estado} - {doc.fecha_recepcion}")
            else:
                messagebox.showerror("Error", "Documento no encontrado.")
            self.menu_documentos()

        button = tk.Button(self.window, text="Buscar Documento", command=buscar)
        button.pack(pady=20)

    def actualizar_estado(self):
        # Ventana para actualizar el estado de un documento
        self._limpiar_ventana()

        tk.Label(self.window, text="ID del documento:").pack(pady=5)
        id_doc = tk.Entry(self.window)
        id_doc.pack(pady=5)

        tk.Label(self.window, text="Nuevo estado:").pack(pady=5)
        nuevo_estado = tk.Entry(self.window)
        nuevo_estado.pack(pady=5)

        def actualizar():
            self.controller.actualizar_estado_documento(int(id_doc.get()), nuevo_estado.get())
            messagebox.showinfo("Información", "Estado actualizado.")
            self.menu_documentos()

        button = tk.Button(self.window, text="Actualizar Estado", command=actualizar)
        button.pack(pady=20)

    def eliminar_documento(self):
        # Ventana para eliminar documento
        self._limpiar_ventana()

        tk.Label(self.window, text="ID del documento a eliminar:").pack(pady=5)
        id_doc = tk.Entry(self.window)
        id_doc.pack(pady=5)

        def eliminar():
            self.controller.eliminar_documento(int(id_doc.get()))
            messagebox.showinfo("Información", "Documento eliminado.")
            self.menu_documentos()

        button = tk.Button(self.window, text="Eliminar Documento", command=eliminar)
        button.pack(pady=20)

    def _limpiar_ventana(self):
        # Limpiar la ventana antes de mostrar una nueva pantalla
        for widget in self.window.winfo_children():
            widget.destroy()

    def iniciar(self):
        self.menu_documentos()  # Llama al menú principal al iniciar
        self.window.mainloop()

# Uso
if __name__ == "__main__":
    # Crear el controlador (se debe ajustar a cómo está definido en tu código)
    controller = DocumentoController()
    app = DocumentoView(controller)
    app.iniciar()
