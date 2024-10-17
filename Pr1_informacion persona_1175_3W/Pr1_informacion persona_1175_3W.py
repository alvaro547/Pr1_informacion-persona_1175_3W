print(" ")
print("Alvaro Campechano 3W")
print(" ")
# Crear un diccionario vacío para almacenar la información de la persona
persona = {}

# Función para agregar datos al diccionario y mostrar su contenido
def agregar_dato(clave, valor):
    persona[clave] = valor
    print(f"Contenido actual del diccionario: {persona}")

# Pedir información al usuario
nombre = input("Ingrese el nombre: ")
agregar_dato("Nombre", nombre)

edad = input("Ingrese la edad: ")
agregar_dato("Edad", edad)

sexo = input("Ingrese el sexo (M/F): ")
agregar_dato("Sexo", sexo)

telefono = input("Ingrese el teléfono: ")
agregar_dato("Teléfono", telefono)

correo = input("Ingrese el correo electrónico: ")
agregar_dato("Correo Electrónico", correo)

# Mostrar el contenido final del diccionario
print("Información completa de la persona:")
print(persona)
