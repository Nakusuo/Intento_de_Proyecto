import tkinter as tk
from src.database import Database
from src.controllers.documento_controller import DocumentoController
from src.view.documento_view import DocumentoView

def main():
    print("Iniciando la aplicación...")
    try:
        db = Database()  # Crear la conexión a la base de datos
        doc_controller = DocumentoController(db)  # Pasar la conexión al DocumentoController

        root = tk.Tk()  # Crear ventana principal de Tkinter
        app = DocumentoView(root, doc_controller)  # Pasar root y controller a la vista
        app.iniciar()  # Iniciar la aplicación
    except Exception as e:
        print(f"Ocurrió un error al iniciar la aplicación: {e}")

if __name__ == "__main__":
    try:
        db = Database()
        controller = DocumentoController(db)
        root = tk.Tk()
        app = DocumentoView(root, controller)
        root.mainloop()  # Método correcto para iniciar la aplicación de Tkinter
    except Exception as e:
        print(f"Ocurrió un error al iniciar la aplicación: {e}")
