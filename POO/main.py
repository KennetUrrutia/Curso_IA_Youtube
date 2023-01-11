from Empleado import Empleado
from Cliente import Cliente


def cargar():
    salir = True
    
    while salir:
        validador = True
        validador2 = True
    
        while validador:
            respuesta = input('Va a ingresar un empleado? >')
            if (respuesta == 'No' or respuesta == 'Si' or respuesta == 'no' or respuesta == 'si'):
                validador = False
            else:
                print('Respuesta invalida')
    
        nombre = input('Ingrese el nombre > ')
        apellido = input('Ingrese el Apellido > ')
        dni = input('Ingrese el DNI > ')
        telefono = input('Ingrese el teléfono > ')

        if respuesta == 'si' or respuesta == 'Si':
            salario = input('Ingrese su salario > ')
            emp = Empleado(nombre, apellido, dni, telefono, int(salario))
            personas.append(emp)
        else:
            tipo = input('Ingrese el tipo de cliente > ')
            cli = Empleado(nombre, apellido, dni, telefono, tipo)
            personas.append(cli)

        while validador2:
            respuesta2 = input('Desea seguir agregando personas? > ')
            if (respuesta2 == 'No' or respuesta2 == 'Si' or respuesta2 == 'no' or respuesta2 == 'si'):
                validador2 = False
                if respuesta2 == 'No' or respuesta2 == 'no':
                    salir = False
            else:
                print('Respuesta invalida')


personas = []
cargar()
for persona in personas:
    print(persona)

# print('Empleado:\n',emp, '\n')
# print('Cliente:\n',cli, '\n')
