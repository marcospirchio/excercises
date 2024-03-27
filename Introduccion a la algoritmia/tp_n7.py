# TP Nro 7
def ejercicio1():
    a = 10
    b = 140
    num = 0
    lista1 = []
    while num != -1:
        num = int(input("Ingrese valores entre 10 y 140, para finalizar ingrese -1: "))
        if a <= num <= b:
            lista1.append(num)
        elif num == -1:
            print("Función finalizada con éxito!")
        else:
            print("Error, número fuera de rango, ingrese un número nuevamente.")
    return lista1

def es_capicua(lista):
    return lista == lista[::-1]

def contarValorLista(lista,valor):
    lista1 = list(lista)
    return lista1.count(valor)

def listaInversa(lista):
    lista1 = list(lista)
    lista2 = lista1[::-1]
    return lista2

def devolverIndice(lista,valor):
    posiciones =[]
    for i in range(len(lista)):
        if lista[i] == valor:
            posiciones.append(i)
    return posiciones

# Llama a la función ejercicio1() una vez y guarda su resultado
listacapicua = ejercicio1()

# Calcula la suma de los números en la lista
suma = sum(listacapicua)
print("La suma de los números en la lista es:", suma)

# Verifica si la lista es capicúa
if es_capicua(listacapicua) == True:
    print('La lista es capicua')

# Verificamos cuantas veces se encuentra el numero en la lista
print(f'El numero se encuentra {contarValorLista(listacapicua, 20)} veces en la lista')

# Imprimimos la lista invertida.
print(listaInversa(listacapicua))

valor_buscado = 20
posiciones = devolverIndice(listacapicua,valor_buscado)
if posiciones:
    print(f"El valor {valor_buscado} se encuentra en las posiciones:", posiciones)
else:
    print(f"El valor {valor_buscado} no se encuentra en la lista.")

#faltan ejs 7/8/9/10/11/12/13/14