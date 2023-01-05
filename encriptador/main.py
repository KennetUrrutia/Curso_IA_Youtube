"""
    letras y acciones
    a agregar texto al contenido
    w reemplazar todo el contenido
    r solamente permite leer el archivo   
"""
# archivo = open('texto.txt', 'a')
# archivo.write('Prueba de guardado en el archivo')
# archivo.close()

# archivo = open('texto.txt', 'r')
# print(archivo.read())

# ----------------------------------------------------------------

# Funcion para encriptar el texto


def encriptar(text):
    textoFinal = ''
    for letra in text:
        asciiLetter = ord(letra)
        asciiLetter += 5
        textoFinal += chr(asciiLetter)
    return textoFinal

# Funcion para desencriptar el texto


def desencriptar(text):
    textoFinal = ''
    for letra in text:
        asciiLetter = ord(letra)
        asciiLetter -= 5
        textoFinal += chr(asciiLetter)
    return textoFinal

# Funcion para encriptar el archivo


def encriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    texto = archivo.read()
    archivo.close()
    textoEncriptado = encriptar(texto)

    archivo = open(rutaArchivo, 'w')
    archivo.write(textoEncriptado)
    archivo.close()
    print('El archivo fue encriptado correctamente')


def desencriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    texto = archivo.read()
    archivo.close()
    textoDesencriptado = desencriptar(texto)

    archivo = open(rutaArchivo, 'w')
    archivo.write(textoDesencriptado)
    archivo.close()
    print('Archivo desencriptado correctamente')


respuestaValida = False

while respuestaValida == False:
    respuestaEoD = input('Presione "E" para encriptar, o presione "D" para desencriptar > ')
    if respuestaEoD != 'E' and respuestaEoD != 'D' and respuestaEoD != 'e' and respuestaEoD != 'd':
        print('Seleccione una respuesta valida')
        continue
    rutaArchivo = input('Ingrese la ruta del archivo > ')
    

    if respuestaEoD == 'E' or respuestaEoD == 'e':
        encriptarArchivo(rutaArchivo)
        respuestaValida = True
    elif respuestaEoD == 'D' or respuestaEoD == 'd':
        desencriptarArchivo(rutaArchivo)
        respuestaValida = True
    else:
        print('Seleccione una respuesta valida')
