from src.app import App  # Importa la clase principal 'App' desde el archivo app.py

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
