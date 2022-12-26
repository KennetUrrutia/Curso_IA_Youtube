#Calculadora de IMC
# IMC = peso / (Altura X altura)
# <19: delgadez
# Entre 20 y 25: normal
# Entre 26 y 30: sobrepeso
# > de 30: obesidad

#Definir una funcion
def calculateIMC ():
    print('Prueba')

#llamar la funcion
calculateIMC()



peso = int(input('Ingrese su peso en kg '))
altura = int(input('Ingrese su altura en cm '))
altura = altura / 100

imc = peso / (altura * altura)

print('Su IMC es de: ' + str(imc))

if imc <= 19:
    print('Estado de delgadez')
if imc >= 20 and imc <= 25:
    print('Estado normal')
if imc >= 26 and imc <= 30:
    print('Estado de sobrepeso')
if imc >= 30:
    print('Estado de obesidad')