import tkinter as tk
from src.database import Database
from src.controllers.documento_controller import DocumentoController
from src.controllers.usuario_controller import UsuarioController
from src.view.documento_view import DocumentoView
from src.view.usuario_view import UsuarioView

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Mesa de Partes")

        db = Database()

        self.documento_controller = DocumentoController(db)
        self.usuario_controller = UsuarioController(db)

        self.documento_frame = tk.Frame(self.root)
        self.usuario_frame = tk.Frame(self.root)

        self.documento_view = DocumentoView(self.documento_frame, self.documento_controller)
        self.usuario_view = UsuarioView(self.usuario_frame, self.usuario_controller)

        self.menu_principal()

    def menu_principal(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        secciones_menu = tk.Menu(menu)
        menu.add_cascade(label="Secciones", menu=secciones_menu)
        secciones_menu.add_command(label="Gestión de Documentos", command=self.show_documento_view)
        secciones_menu.add_command(label="Gestión de Usuarios", command=self.show_usuario_view)
        secciones_menu.add_command(label="Salir", command=self.root.quit)

        self.show_documento_view()

    def show_documento_view(self):
        self.usuario_frame.pack_forget()
        self.documento_frame.pack(fill="both", expand=True)

    def show_usuario_view(self):
        self.documento_frame.pack_forget()
        self.usuario_frame.pack(fill="both", expand=True)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
