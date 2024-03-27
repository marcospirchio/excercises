#Ejercicio 1
edad = int(input('Ingrese la eddad de la persona, si desea terminar ingrese -1: '))
menores_edad = []
mayores_edad = []
total_menores = 0
total_mayores = 0
while edad != -1:
     if 0 <= edad <= 100:
          if edad >= 18:
             mayores_edad.append(edad)
             total_mayores += 1
          elif edad < 18:
             menores_edad.append(edad)
             total_menores += 1
     else:
          print('La edad no es valida')
          edad = int(input('Ingrese la eddad de la persona, si desea terminar ingrese -1: '))
     edad = int(input('Ingrese la eddad de la persona, si desea terminar ingrese -1: '))
print(f'Hay {total_menores} menores de edad')
print(f'Hay {total_mayores} mayores de edad')
if total_mayores > 0:
    promedio_mayores = sum(mayores_edad) / total_mayores
    print(f'El promedio de los menores de edad es de: {round(promedio_mayores,2)} años')
if total_menores > 0:
    promedio_menores = sum(menores_edad) / total_menores
    print(f'El promedio de los menores de edad es de: {round(promedio_menores,2)} años')

#Ejercicio 2
legajo = int(input('Ingrese su numero de legajo, para finalizar ingrese -1: '))
print(f'Bienvenido {legajo}! ')
alumnos_aprobados = 0
alumnos_desaprobados = 0
alumnos_aplazados = 0
while legajo != -1:
    nota = int(input('Ingrese su nota de examen final: '))
    if 1 <= nota <= 10:
        if nota >= 4:
            alumnos_aprobados += 1
            print('Has aprobado el examen final')
        elif 1 < nota < 4:
            alumnos_desaprobados += 1
            print('Has desaprobado el examen, tu nota es menor a 4')
        elif nota ==1:
            alumnos_aplazados += 1
            print('Has aplazado el examen, tu nota es igual a 1')
    else:
        print('Nota invalida, debe ingresar un valor entre 1 y 10')
    legajo = int(input('Ingrese su numero de legajo, para finalizar ingrese -1: '))
    print(f'Bienvenido {legajo}! ')
print(f'Hay {alumnos_aprobados} alumnos aprobados')
print(f'Hay {alumnos_desaprobados} alumnos desaprobados')
print(f'Hay {alumnos_aplazados} alumnos aplazados')

#Ejercicio 3
cant_producto = int(input('Ingrese la cantidad del producto solicitado: '))
while cant_producto != 1:
    if 1 <= cant_producto <= 12:
        precio_base = int(input('Ingrese el precio base de cada producto: '))
        valor_final = round(precio_base * cant_producto)
        promedio = round(valor_final/cant_producto,2)
        print(f'Valor total de la venta: {valor_final}\nPrecio promedio por unidad: {promedio}')
    elif 13 <= cant_producto <= 100:
        precio_base = int(input('Ingrese el precio base de cada producto: '))
        valor_final = round((precio_base*cant_producto)*0.9,2)
        promedio = round(valor_final/cant_producto,2)
        print(f'Valor total de la venta: {valor_final}\nPrecio promedio por unidad: {promedio}')
    elif cant_producto >= 101:
        precio_base = int(input('Ingrese el precio base de cada producto: '))
        valor_final = round((precio_base*cant_producto)*0.75,2)
        promedio = round(valor_final/cant_producto,2)
        print(f'Valor total de la venta: {valor_final}\nPrecio promedio por unidad: {promedio}')
    elif cant_producto == -1:
        break
    cant_producto = int(input('Ingrese la cantidad del producto solicitado: '))
print('Finalizado con éxito!')

#Ejercicio 4
nro_cliente = int(input('Ingrese su numero de cliente: '))
total_factura = int(input('Ingrese el valor total de su factura: '))
# 1 al 10
print('\nSi paga del dia 1 al 10 de este mes:')
if 200 > (total_factura*0.02):
    print(f'Su factura es de: {round(total_factura-200,2)}\nSe le realiza un descuento de $200 ')
elif 200 < (total_factura*0.02):
    descuento = total_factura*0.98
    print(f'Su factura es de: {round(descuento)}\nSe le realiza un descuento de {round(total_factura*0.02,2)} ')
# 11 al 20
print('\nSi paga del dia 11 al 20 de este mes:')
print(f'Debes pagar el importe original de la factura: {total_factura}')
# 21 al fin de mes
print('\nSi paga del dia 20 de este mes, en adelante:')

if 350 > (total_factura*0.10):
    multa = total_factura+350
    print(f'El importe de su factura es de: {multa}\nTiene incluida una multa de $350 por pago fuera de termino.')
elif 350 < (total_factura*0.10):
    multa = total_factura*1.10
    print(f'El importe de su factura es de: {round(multa)}\nTiene incluida una multa de: {round(total_factura*0.1,2)}')

#Ejercicio 5
#No se

#Ejercicio 6
nummero = input('Ingrese un numero para informar cuantos digitos tiene: ')
digito = 0
for letra in nummero:
    digito += 1
if "-" in nummero:
    digito -= 1

print(f'Tiene {digito} digitos')

#Ejercicio 7
#No se

#Ejercicio 8
legajoo = input('Ingrese su legajo. Para finalizar, ingrese -1: ')
salario = 0
salario2 = 0
salario3 = 0
sueldo_cat1 = 0
sueldo_cat2 = 0
sueldo_cat3 = 0
salarios_total = 0
cant_sueldos = 0
dic = {}
while legajoo != -1:
    categoria = int(input('Ingrese su categoria, entre 1 y 3: '))
    if 0 < categoria < 4:
        if categoria == 1:
            salario = int(input('Ingrese su salario: '))
            sueldo_cat1 = sueldo_cat1 + salario
        elif categoria == 2:
            salario = int(input('Ingrese su salario: '))
            sueldo_cat2 = sueldo_cat2 + salario
        elif categoria == 3:
            salario = int(input('Ingrese su salario: '))
            sueldo_cat3 = sueldo_cat3 + salario
            if salario < 50000:
                salario3 += 1
        if salario > 200000:
            salario2 += 1

    else:
        print('Categoria incorrecta, ingrese un valor entre 1 y 3')
    dic[legajoo] = salario
    salarios_total = salarios_total + salario
    cant_sueldos += 1
    legajoo = int(input('Ingrese su legajo. Para finalizar, ingrese -1: '))

s_promedio = round(salarios_total / cant_sueldos,1)
salario_maximo = max(dic.values())
salario_minimo = min(dic.values())
clave_salario_maximo = None
for clave, valor in dic.items():
    if valor == salario_maximo:
        clave_salario_maximo = clave
        print(f'El legajo del empleado que mas gana es: {clave_salario_maximo}')
        break
print(f'El importe total de los salarios pagados por la empresa es de: ${salarios_total}')
print(f'La cantidad de empleados que ganan mas de $200.000 son: {salario2}')
print(f'La cantidad de empleados que ganan menos de $50000, y su categoría es 3: {salario3}')
print(f'El sueldo del empleado que menos gana es: {salario_minimo}')
print(f'El importe total de sueldos por categoria es:\nCat 1: ${sueldo_cat1}\nCat 2: ${sueldo_cat2}\nCat 3: ${sueldo_cat3}')
print(f'El salario promedio de la empresa es de ${s_promedio}')

#Ejercicio 9
sumai = 0
N = int(input('Ingresa un valor positivo: '))
if N > 0:
    for i in range(1, (N+1)):
        if i % 2 == 1:
            print(i)
        else:
            continue
        sumai = sumai + i
else:
    print('Erorr, el numero tiene que ser positivo.')
print(f'La suma de los impares hasta llegar a {N} es: {sumai}')


