#Ejercicio 1
num = int(input('Ingrese los numeros que desee, para terminar ingrese -1: '))
lista_num = []
while num != -1:
    lista_num.append(num)
    num = int(input('Ingrese un numero, para terminar ingrese -1: '))

print(f'El primer numero ingresado fue: {lista_num[0]}, y el ultimo numero fue: {lista_num[-1]}')

#Ejercicio 2
num1 = int(input('Ingrese los numeros que desee, para terminar ingrese -1: '))
num_ingresado = 0
while num1 != -1:
    num_ingresado += 1
    num1 = int(input('Ingrese un numero, para terminar ingrese -1: '))

if num_ingresado % 2 == 0:
    print('La cantidad de numeros ingresados es PAR')
elif num_ingresado % 2 == 1:
    print('La cantidad de numeros ingresados es IMPAR')

#Ejercicio 3
num2 = int(input('Ingrese los numeros que desee, para terminar ingrese -1: '))
lista_num1 = []
while num2 != -1:
    lista_num1.append(num2)
    num2 = int(input('Ingrese un numero, para terminar ingrese -1: '))

print(f'El numero mas chico ingresado a la lista es: {min(lista_num1)}')
print(f'El numero mas grande ingresado a la lista es: {max(lista_num1)}')

#Ejercicio 4
for n in range (42, 177):
    if n % 2 == 0:
        pass
    elif n % 2 == 1:
        print(n)

#Ejercicio 5
n_inic = int(input('A continuacion se imprimiran numeros hasta el numero que ingreses: '))
for x in range(1,(n_inic + 1)):
    print(x)

#Ejercicio 6
for m in range(1,13):
    print(m,':',4*m)

decision = int(input('Ingrese 1 si desea consultar la tabla de otro numero, o cualquier numero si desea salir: '))
while decision == 1:
    tabla = int(input('Ingrese un numero para consultar su tabla: '))
    for p in range(1,13):
        print(p, ':', (tabla * p))
    decision = int(input('Ingrese 1 si desea consultar la tabla de otro numero, o cualquier numero si desea salir: '))

print('Sesion finalizada')

#Ejercicio 7
lista1 = []
cant_numero = 0
suma_numero = 0
while cant_numero <= 10:
    numero = int(input('Ingrese un numero (se ingresaran 10 numeros): '))
    cant_numero += 1
    suma_numero += numero
    lista1.append(numero)

promedio = (suma_numero / 10)
print(f'El promedio de los numeros sumados es: {round(promedio,2)}')
print(f'El numero mas grande ingresado es: {max(lista1)}')
print(f'El numero mas grande fue ingresado en la posicion: {lista1.index(max(lista1))}')

#Ejercicio 8
suma_de_numeros = 0
cantidad_num = 0
while suma_de_numeros <= 100:
    numm = int(input('Ingrese numeros, solo se sumaran los pares, hasta que la suma pase los 100: '))
    cantidad_num += 1
    if numm % 2 == 0:
        suma_de_numeros += numm
    else:
        pass
print(f'Se ingresaron {cantidad_num} numeros')
print(suma_de_numeros)

#Ejercicio 9
pares = 0
impares = 0
patente = int(input('Ingrese la terminacion de la patente (entre 0 y 9, para finalizar -1): '))
while patente != -1:
    if 0 <= patente <= 9:
        if patente % 2 == 0:
            pares += 1
            print(f'{patente} es par')
        elif patente % 2 == 1:
            impares += 1
            print(f'{patente} es impar')

    else:
        print('Numero invalido, debe terminar en un numero del 0 al 9')
    patente = int(input('Ingrese la terminacion de la patente (entre 1 y 9, para finalizar -1): '))


print(f'Pasaron {pares} vehiculos con numeracion par')
print(f'Pasaron {impares} vehiculos con numeracion impar')

#Ejercicio 10
#paja

#Ejercicio 11
# No pude

#Ejercicio 12
num_uno = 0
num_dos = 1
sumanum = num_uno + num_dos
numm= int(input('ingrese un numero: '))
for i in range(0,numm):
     print(num_uno)
     print(num_dos)
     num_uno = num_uno + num_dos
     num_dos = num_uno + num_dos
print(sumanum)