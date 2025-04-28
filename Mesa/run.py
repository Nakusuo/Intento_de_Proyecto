import sys
import os

# Añadir el directorio raíz al sys.path para que Python encuentre 'config' y 'src'
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.app import App  # Ahora debería funcionar

def iniciar_aplicacion():
    try:
        # Si tu aplicación tiene alguna lógica inicial (conexión a base de datos, configuración, etc.), la llamas aquí.
        print("Iniciando la aplicación...")

        # Crea una instancia de la aplicación y ejecuta el método run()
        app = App()  # Crea la instancia de la aplicación
        app.run()    # Ejecuta la aplicación

    except Exception as e:
        print(f"Ocurrió un error al iniciar la aplicación: {e}")

if __name__ == "__main__":
    iniciar_aplicacion()  # Llama a la función para iniciar la aplicación
