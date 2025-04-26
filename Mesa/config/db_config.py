class Config:
    """Configuración general de la aplicación."""
    APP_NAME = "Sistema Mesa de Partes"
    VERSION = "1.0"
    DEBUG = True

    # Parámetros de conexión a la base de datos
    DB_HOST = 'localhost'  # Dirección del servidor SQL Server
    DB_NAME = 'NakusuDB'   # Nombre de la base de datos
    DB_USER = 'sa'         # Usuario de la base de datos
    DB_PASSWORD = 'TuContraseñaSegura'  # Contraseña del usuario
