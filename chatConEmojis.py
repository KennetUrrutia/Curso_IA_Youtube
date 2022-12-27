texto = ''
while texto != 'salir': 
    texto = input('> ')
    texto = texto.replace(':)','😊')
    texto = texto.replace(':(','😕')
    texto = texto.replace(';)','😉')
    texto = texto.replace(':p','😛')
    texto = texto.replace(';p','😜')
    texto = texto.replace('XD','😆')
    texto = texto.replace('xp','😝')
    print(texto)
