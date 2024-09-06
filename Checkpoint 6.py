class Usuario:
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña

    def mostrar_info(self):
        print(f"Nombre de Usuario: {self.nombre_usuario}")

usuario1 = Usuario("Nayra Leon", "mi_contraseña_segura")

usuario1.mostrar_info()

