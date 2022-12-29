diccionario = {
    "programar" : "programar es transfomar en codigo una idea",
    "POO" : "Programacion orientada a objetos",
    "MVC" : "Modelo Vista Controlador"
}

print(diccionario["programar"])

#Ejercicio 
numero = input('Escribe un numero \n> ')

diccionary = {
    '0':'cero',
    '1':'uno',
    '2':'dos',
    '3':'tres',
    '4':'cuatro',
    '5':'cinco',
    '6':'seis',
    '7':'siete',
    '8':'ocho',
    '9':'nueve',
}

textoFinal = ''

for letra in numero:
    textoFinal += diccionary[letra]+ ' '

print(textoFinal)