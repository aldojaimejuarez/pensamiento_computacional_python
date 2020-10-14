def primera_letra(lista_palabras):
  
    primeras_letras = []

    for palabra in lista_palabras:

        assert type(palabra) == str, f'{palabra} no es un string'
        assert len(palabra) > 0, 'No se permiten espacios vacíos'


        primeras_letras.append(palabra[0])

    print(primeras_letras)
    

lista_palabras = [5,'aldo', 'caro','']


if __name__ == '__main__':
    primera_letra(lista_palabras)

