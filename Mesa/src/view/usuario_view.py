import tkinter as tk
from tkinter import messagebox

class UsuarioView:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Gestión de Usuarios")

        # Título principal
        self.label = tk.Label(parent, text="Gestión de Usuarios", font=("Arial", 16))
        self.label.pack(pady=10)

        # Nombre de Usuario
        self.nombre_label = tk.Label(parent, text="Nombre de Usuario:")
        self.nombre_label.pack(pady=5)
        self.nombre_entry = tk.Entry(parent)
        self.nombre_entry.pack(pady=5)

        # Rol del Usuario
        self.rol_label = tk.Label(parent, text="Rol del Usuario:")
        self.rol_label.pack(pady=5)
        self.rol_entry = tk.Entry(parent)
        self.rol_entry.pack(pady=5)

        # Botón para crear usuario
        self.crear_button = tk.Button(parent, text="Crear Usuario", command=self.crear_usuario)
        self.crear_button.pack(pady=10)

    def crear_usuario(self):
        nombre = self.nombre_entry.get()
        rol = self.rol_entry.get()

        if not nombre or not rol:
            messagebox.showerror("Error", "Por favor, ingrese todos los campos.")
            return

        # Aquí iría la lógica de crear el usuario, por ejemplo, guardarlo en una base de datos
        # En este caso, simplemente imprimimos los datos para ver que funciona
        print(f"Crear usuario: {nombre}, rol: {rol}")

        # Mostrar mensaje de confirmación
        messagebox.showinfo("Usuario Creado", f"Usuario '{nombre}' con rol '{rol}' creado correctamente.")
        
        # Limpiar los campos de entrada
        self.nombre_entry.delete(0, tk.END)
        self.rol_entry.delete(0, tk.END)

# Configuración de la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = UsuarioView(root)
    root.mainloop()
