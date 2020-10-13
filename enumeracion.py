def run():
    # objetivo = int(input('Escoge un número entero y te regreso su raiz cuadrada exacta: '))
    # respuesta = 0

    # while respuesta**2 < objetivo:
    #     respuesta += 1
    
    # if respuesta**2 == objetivo:
    #     print(f'La raiz cuadrada de {objetivo} es {respuesta}')

    # else:
    #     print(f'{objetivo} no tiene raiz cuadrada exacta')


        objetivo = int(input('Escoge un número entero y te regreso su raiz cúbica exacta: '))
        respuesta = 0

        while respuesta**3 < objetivo:
            respuesta += 1
    
        if respuesta**3 == objetivo:
            print(f'La raiz cúbica de {objetivo} es {respuesta}')

        else:
            print(f'{objetivo} no tiene cúbica cuadrada exacta')

if __name__ == '__main__':
    run()