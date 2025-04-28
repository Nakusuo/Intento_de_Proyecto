from src.database import Database
from src.controllers.documento_controller import DocumentoController
from src.view.documento_view import DocumentoView

def main():
    print("Iniciando la aplicación...")
    try:
        db = Database()  # Crear la conexión a la base de datos
        doc_controller = DocumentoController(db)  # Pasar la conexión al DocumentoController
        app = DocumentoView(doc_controller)  # Pasar el controller a la vista
        app.iniciar()
    except Exception as e:
        print(f"Ocurrió un error al iniciar la aplicación: {e}")

if __name__ == "__main__":
    main()
