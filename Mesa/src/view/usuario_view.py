from src.controllers.usuario_controller import UsuarioController

class UsuarioView:
    def __init__(self, controller: UsuarioController):
        self.controller = controller

    def menu_usuarios(self):
        while True:
            print("\n--- Gestión de Usuarios ---")
            print("1. Crear Usuario")
            print("2. Listar Usuarios")
            print("3. Buscar Usuario por ID")
            print("4. Actualizar Rol de Usuario")
            print("5. Eliminar Usuario")
            print("6. Volver al Menú Principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.crear_usuario()
            elif opcion == "2":
                self.listar_usuarios()
            elif opcion == "3":
                self.buscar_usuario()
            elif opcion == "4":
                self.actualizar_rol()
            elif opcion == "5":
                self.eliminar_usuario()
            elif opcion == "6":
                break
            else:
                print("Opción inválida.")

    def crear_usuario(self):
        nombre = input("Nombre de usuario: ")
        rol = input("Rol del usuario: ")
        usuario = self.controller.crear_usuario(nombre, rol)
        print(f"Usuario creado con ID: {usuario.id_usuario}")

    def listar_usuarios(self):
        usuarios = self.controller.listar_usuarios()
        for user in usuarios:
            print(f"{user.id_usuario} - {user.nombre_usuario} - {user.rol}")

    def buscar_usuario(self):
        id_user = int(input("Ingrese ID del usuario: "))
        user = self.controller.obtener_usuario_por_id(id_user)
        if user:
            print(f"Usuario: {user.nombre_usuario} - Rol: {user.rol}")
        else:
            print("Usuario no encontrado.")

    def actualizar_rol(self):
        id_user = int(input("ID del usuario: "))
        nuevo_rol = input("Nuevo rol: ")
        self.controller.actualizar_rol_usuario(id_user, nuevo_rol)
        print("Rol actualizado.")

    def eliminar_usuario(self):
        id_user = int(input("ID del usuario a eliminar: "))
        self.controller.eliminar_usuario(id_user)
        print("Usuario eliminado.")
