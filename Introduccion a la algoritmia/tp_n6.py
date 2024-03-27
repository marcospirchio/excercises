#Practica ppt funciones
texto = "Esta es la materia Introducción a la Algoritmia, comenzamos con los fundamentos de programación."

def cantCaracteres():
    print(f'La cantidad de caracteres de la cadena es: {len(texto)}')

def pasarMayus():
    print(texto.upper())

def pasarMinus():
    print(texto.lower())

def reemplazarPalabra():
    print(texto.replace("comenzamos con","en la unidad 1 vemos"))

cantCaracteres()
pasarMayus()
pasarMinus()
reemplazarPalabra()

#Practica de parametros:
def calcularPromedio(a,b):
    prom = (a+b)/2
    return prom

x=int(input("Ingrese un numero entero: "))
y=int(input("Ingrese otro numero entero: "))
resultado=calcularPromedio(x,y)
print("El promedio de ",x,"y",y,"es",resultado)


#Ejercicio 1
def ejercicio1(a,b):
    resultado = 0
    for i in range(b):
        resultado += a
    return resultado


d= int(input('numero1: '))
e= int(input('numero1: '))
resultado = ejercicio1(d, e)
print(resultado)

#Ejercicio 2
def ejercicio2(a,b):
    resultado = 1
    for i in range(b):
        resultado = resultado * a
    print(resultado)

e = int(input("Ingresa numero: "))
f = int(input("Ingresa numero: "))
ejercicio2(e,f)

#Ejercicio 3
def ejercicio3(g):
    for i in range(g):
        print("*")

h = int(input("Ingrese un numero de columnas: "))
ejercicio3(h)

#Ejercicio 4
def ejercicio4(a,b):
    if a % b == 0:
        return True
    else:
        return False
print(ejercicio4(20,5))

#Ejercicio 5
def signo(n):
    if n > 0:
        print(f'1 (valor positivo)')
    elif n == 0:
        print(f'0 (valor neutro)')
    elif n < 0:
        print(f'-1 (valor negativo)')
signo(14)
signo(0)
signo(-14)

#Ejercicio 6
def comparar(a,b):
    if a > b:
        print('1 (el valor 1 es mayor al valor 2)')
    elif a == b:
        print('0 (ambos valores son iguales)')
    elif a < b:
        print('-1 (el valor 2 es mayor que el valor 1)')

comparar(4,2)
comparar(4,4)
comparar(2,4)

#Ejerciciio 10
def extraer_digito(numero, posicion):
    numero_str = str(numero)
    longitud = len(numero_str)
    posicion_desde_la_derecha = longitud - 1 - posicion
    if 0 <= posicion_desde_la_derecha < longitud:
        digito = int(numero_str[posicion_desde_la_derecha])
        return digito
    else:
        return -1

print(extraer_digito(12345, 1))  # Devuelve 4
print(extraer_digito(12345, 8))  # Devuelve -1

#Ejercicio 11
def obtenerNumCentro(a):
    numero_str = str(a)
    longitud = len(numero_str)-1
    digitos = longitud - 1
    medio = round((longitud + 0.1) / 2)
    if digitos % 2 == 0:
        return "La cantidad de digitos dehe ser impar"
    elif digitos % 2 == 1:
        return numero_str[medio]
print(f'El numero del medio es: {obtenerNumCentro(123456789101111)}')
