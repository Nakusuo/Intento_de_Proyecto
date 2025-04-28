import tkinter as tk
from tkinter import messagebox
from src.controllers.usuario_controller import UsuarioController

class UsuarioView:
    def __init__(self, parent, controller: UsuarioController):
        self.controller = controller
        self.parent = parent

        self.label = tk.Label(parent, text="Gestión de Usuarios", font=("Arial", 16))
        self.label.pack(pady=10)

        self.nombre_label = tk.Label(parent, text="Nombre de Usuario:")
        self.nombre_label.pack(pady=5)
        self.nombre_entry = tk.Entry(parent)
        self.nombre_entry.pack(pady=5)

        self.rol_label = tk.Label(parent, text="Rol del Usuario:")
        self.rol_label.pack(pady=5)
        self.rol_entry = tk.Entry(parent)
        self.rol_entry.pack(pady=5)

        self.crear_button = tk.Button(parent, text="Crear Usuario", command=self.crear_usuario)
        self.crear_button.pack(pady=10)

    def crear_usuario(self):
        nombre = self.nombre_entry.get()
        rol = self.rol_entry.get()

        if not nombre or not rol:
            messagebox.showerror("Error", "Por favor, ingrese todos los campos.")
            return

        usuario = self.controller.crear_usuario(nombre, rol)

        messagebox.showinfo("Usuario Creado", f"Usuario '{usuario.nombre_usuario}' con rol '{usuario.rol}' creado correctamente.")
        
        self.nombre_entry.delete(0, tk.END)
        self.rol_entry.delete(0, tk.END)
