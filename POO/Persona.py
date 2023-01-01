class Persona:
    def __init__(self, nombre, apellido, dni, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono

    def __str__(self):
        text = 'Nombre: ' + self.nombre + '\n ' + 'Apellidos: ' + \
            self.apellido + '\n ' + 'DNI:' + self.dni + '\n ' + \
            'telefono: ' + self.telefono
        return text
