import datetime

def validar_fecha(fecha_str):
    """Valida que la fecha sea en formato YYYY-MM-DD."""
    try:
        datetime.datetime.strptime(fecha_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def formatear_fecha_actual():
    """Devuelve la fecha actual en formato YYYY-MM-DD."""
    return datetime.datetime.now().strftime("%Y-%m-%d")

def validar_opcion_menu(opcion, opciones_validas):
    """Valida que la opción ingresada esté en la lista de opciones válidas."""
    return opcion in opciones_validas

def limpiar_texto(texto):
    """Quita espacios en blanco al inicio y final del texto."""
    return texto.strip()

def confirmar_accion(mensaje):
    """Pide al usuario confirmar una acción (Sí o No)."""
    respuesta = input(f"{mensaje} (s/n): ").lower()
    return respuesta == "s"
