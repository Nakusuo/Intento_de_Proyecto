import tkinter as tk
from src.view.documento_view import DocumentoView
from src.view.usuario_view import UsuarioView

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Mesa de Partes")
        
        # Crear frames para cada vista
        self.documento_frame = tk.Frame(self.root)
        self.usuario_frame = tk.Frame(self.root)

        # Inicializar vistas
        self.documento_view = DocumentoView(self.documento_frame)
        self.usuario_view = UsuarioView(self.usuario_frame)

        # Mostrar la vista de documentos por defecto
        self.show_documento_view()

    def show_documento_view(self):
        """Muestra la vista de documentos y oculta la de usuarios"""
        self.usuario_frame.pack_forget()
        self.documento_frame.pack(fill="both", expand=True)

    def show_usuario_view(self):
        """Muestra la vista de usuarios y oculta la de documentos"""
        self.documento_frame.pack_forget()
        self.usuario_frame.pack(fill="both", expand=True)

    def run(self):
        self.root.mainloop()
