import tkinter as tk
from view import documento_view
from view import usuario_view

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Mesa de Partes")
        
        # Inicializar vistas
        self.view = documento_view(self.root)
        self.view = usuario_view(self.root)

    def run(self):
        self.root.mainloop()
