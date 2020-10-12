def run():
    # num_1 = int(input('Escoge un entero: '))
    # num_2 = int(input('Escoge otro entero: '))

    # if num_1 > num_2:
    #     print('El primer número es mayor al segundo')
    # elif num_1 < num_2:
    #     print('El segundo número es mayor al primero')
    # else:
    #     print('Los números son iguales')

    nombre1 = input('Ingresa tu nombre: ')
    edad1 = int(input(nombre1 + ' ingresa tu edad: '))
    nombre2 = input('Segunda persona, ingresa tu nombre: ')
    edad2 = int(input(nombre2 + ' ingresa tu edad: '))

    if edad1 > edad2:
        # print(nombre1 + " es mayor que " + nombre2)
        print(f'{nombre1} es mayor que {nombre2}')
    elif edad1 < edad2:
        # print(nombre2 + " es mayor que " + nombre1)
        print(f'{nombre2} es mayor que {nombre1}')
    else:
        print(f'{nombre1} y {nombre2}  tiene la misma edad')

        
if __name__ == '__main__':
    run()

