import random

# Programa de reservas de butacas de cine

def sala_butacas():
    matriz = []
    filas = 5  # filas de la sala
    butacas = 7  # butacas por fila
    for f in range(filas):
        matriz.append([0] * butacas)

    return matriz


def cargar_sala(matriz):
    # Ej 1a
    # Llena la matriz con valores aleatorios
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c] = random.randint(0, 1)

    return matriz


def mostrar_butacas(matriz):
    print('*****************************************************')
    print('Butacas con valor 0 estan libres, butacas con valor 1 estan reservadas')
    print('   -------------------Pantalla-------------------- ')
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            print("%6d" % matriz[f][c], end=" ")  # "%6d" % agrega un espaciado de 6 digitos
        print()
    print('*****************************************************')
    print(f'Butacas libres restantes en la sala: {butacas_libres(sala)}')
    print(f'Mayor cantidad de butacas contiguas: {butacas_contiguas(sala)}')
    print('*****************************************************')


def reservar(matriz, filas, butacas):
    if filas < 0 or filas >= len(matriz):
        print('Fila invalida, debes ingresar una de valor 1 al 5')

        return matriz
    else:
        if butacas < 0 or butacas >= len(matriz[0]):
            print("Ubicacion de butaca invalida. Ingrese una butaca del 1 al 7")

            return matriz

    if matriz[filas][butacas] == 0:
        matriz[filas][butacas] = 1
        print('Butaca reservada')
    elif matriz[filas][butacas] == 1:
        print('La butaca ya se encuentra reservada, intente en otro asiento')

    return matriz


def butacas_libres(matriz):
    asientos_libres = 0
    for fila in matriz:
        for asiento in fila:
            if asiento == 0:
                asientos_libres += 1
            else:
                pass

    return asientos_libres


def butacas_contiguas(matriz):
    mas_butacas_seguidas = 0
    for fila in matriz:
        butacas_seguidas = 0
        for asiento in fila:
            if asiento == 0:
                butacas_seguidas += 1
            else:
                if butacas_seguidas > mas_butacas_seguidas:
                    mas_butacas_seguidas = butacas_seguidas
                butacas_seguidas = 0  # reinicia el contador a 0 cuando el valor del asiento es 1

        if butacas_seguidas > mas_butacas_seguidas:
            mas_butacas_seguidas = butacas_seguidas

    return mas_butacas_seguidas


# ---------------------- CODIGO PRINCIPAL ----------------------

# Creamos la matriz
sala_vacia = sala_butacas()

# Cargamos los valores de las butacas
sala = cargar_sala(sala_vacia)

condicion = ''
while condicion != 0:
    condicion = int(input('Desea reservar un asiento? SI: 1 // NO: 0.  '))
    if condicion == 1:
        print()
        print('Bienvenido a la reserva de butacas del cine!')
        mostrar_butacas(sala)

        # ingresa fila y butaca  a reservar
        reserva_fila = int(input('Ingresa la fila donde se encuentra su butaca a reservar: ')) - 1
        reserva_butaca = int(input('Ingresa la butaca a reservar: ')) - 1

        # realiza reserva
        reservar(sala, reserva_fila, reserva_butaca)

        # muestra la sala actualizada
        mostrar_butacas(sala)

    elif condicion == 0:
        print('Proceso finalizado')
        break

    else:
        print('Valor invalido, solo puede ingresar 1 si desea reservar una butaca, o 0 si no lo desea.')
