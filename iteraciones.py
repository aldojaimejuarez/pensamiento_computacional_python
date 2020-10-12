def run():
    # contador = 0

    # while contador <= 10:
    #     print(contador)
    #     contador += 1 # es igual a contador + 1


    # contador_interno = 0
    # contador_externo = 0

    # while contador_externo <= 5:
    #     while contador_interno <= 6:
    #         print(contador_externo, contador_interno)
    #         contador_interno += 1 
    #         if contador_interno >= 3:
    #             break


    #     contador_externo += 1  #Está en el mismo bloque que el contador_externo
    #     contador_interno = 0  #si no lo ponemos en cero, ya no entraría por que ya es mayor que 6
    #     if contador_externo >= 3:
    #         break
    frase = input('Escribe una frase: ')
    for caracter in frase:
        print(caracter.upper())


if __name__ == '__main__':
    run()