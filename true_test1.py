# Sistema básico de registro y login en consola

usuarios = {}  # Aquí guardaremos usuario: contraseña

def registrar_usuario():
    print("\n--- Registro ---")
    username = input("Elige un nombre de usuario: ")
    
    if username in usuarios:
        print("Ese usuario ya existe. Intenta con otro.")
        return
    
    password = input("Elige una contraseña: ")
    usuarios[username] = password
    print("Usuario registrado exitosamente.\n")

def iniciar_sesion():
    print("\n--- Login ---")
    username = input("Usuario: ")
    password = input("Contraseña: ")

    if username in usuarios and usuarios[username] == password:
        print("Inicio de sesión exitoso. ¡Bienvenido!\n")
    else:
        print("Usuario o contraseña incorrectos.\n")

def menu():
    while True:
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta nuevamente.\n")

if __name__ == "__main__":
    menu()
