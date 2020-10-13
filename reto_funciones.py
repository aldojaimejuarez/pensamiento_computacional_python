def run():
    algoritmo = int(input('Elige un algoritmo para encontrar la raiz cuadrada: Escribe el número 1 para enumeración exhaustiva, 2 para aproximación y 3 para búsqueda binaria: '))

    if algoritmo == 1:
        print('Elegiste enumeración exhaustiva')
        objetivo = int(input('Escoge un número entero y te regreso su raiz cuadrada exacta: '))
        respuesta = 0

        while respuesta**2 < objetivo:
            respuesta += 1

        if respuesta**2 == objetivo:
            print(f'La raiz cuadrada de {objetivo} es {respuesta}')

        else:
            print(f'{objetivo} no tiene raiz cuadrada exacta')


    elif algoritmo == 2:
        print('Elegiste aproximación')
        objetivo = int(input('Escoge un número: '))
        epsilon = 0.01
        paso = epsilon**2
        respuesta = 0.0

        while abs(respuesta**2 - objetivo) > epsilon and respuesta <= objetivo:
            respuesta += paso

        if abs(respuesta**2 - objetivo) >= epsilon:
            print(f'No se encontró la raiz cuadrada de {objetivo}')

        else:
            print(f'La raiz cuadrada de {objetivo} es {respuesta}')


    elif algoritmo == 3:
        print('Elegiste búsqueda binaria')
        objetivo = int(input('Escoge un número: '))
        epsilon = 0.001
        bajo = 0.0
        alto = max(1.0, objetivo)
        respuesta = (alto + bajo) / 2

        while abs(respuesta**2 - objetivo) >= epsilon:
            if respuesta**2 < objetivo:
                bajo = respuesta

            else:
                alto = respuesta

            respuesta = (alto + bajo) / 2

        print(f'La raiz cuadrada de {objetivo} es {respuesta}')


    else:
        print('Escoge una opción correcta.')
        run()

if __name__ == '__main__':
    run()