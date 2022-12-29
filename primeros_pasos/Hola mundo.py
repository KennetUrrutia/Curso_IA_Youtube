nombre = 'Kennet'
edad = 18

texto = 'Hola mundo, soy ' + nombre + ' y tengo ' + str(edad) + ' anios'

print(texto)

nombre2 = input('Como te llamas? ')
edad2 = int(input('Que edad tienes? '))

print('Hola ', nombre2)

if edad2 >= 18:
    print('Es mayor de edad')
else:
    print('Es menor de edad')

