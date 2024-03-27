#Ejercicio 1
a = int(input('ingresa un numero: '))
b = int(input('ingresa un numero: '))
if a == b:
    print('los numeros son iguales')
elif a != b:
    print('los numeros son distintos')

#Ejercicio 2
aa = int(input('ingresa un numero: '))
if aa % 2 == 0:
    print('El numero es par')
elif aa % 2 == 1:
    print('El numero es impar')

# Ejercicio 3
numero = int(input('ingresa un numero del 1 al 12, correspondiente a un mes: '))
if 1 <= numero <= 12:
    meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    nombre_mes = meses[numero - 1] #EJ numero = 1. quedaria meses = [1-1] osea meses =[0], correspodniente al mes de enero
    print("El nombre del mes es:", nombre_mes)
else:
     print('Numero invalido, ingrese nuevamente un numero entre 1 y 12')

#Ejercicio 4
parcial1 = int(input('Ingresar nota correspondiente al parcial 1: '))
parcial2 = int(input('Ingresar nota correspondiente al parcial 2: '))

if parcial1 >= 7 and parcial2 >= 7:
    print('El alumno promociono la materia')
elif 4 <= parcial1 <= 10 and 4 <= parcial2 < 7:
    print('El alumno aprobo la cursada')
elif 4 <= parcial1 < 7 and 4 <= parcial2 <= 10:
    print('El alumno aprobo la cursada')
elif parcial1 < 4 or parcial2 < 4:
    print('El alumno debe recuperar la cursada')

#Ejercicio 5
costo_basico = 500
costo_pagina = 3.20
tela = 200
encuadernacion_especial = 336
cant_pagina = int(input('Ingrese la cantidad de paginas a imprimir: '))
precioLibro = costo_basico + (cant_pagina * costo_pagina)
if cant_pagina < 300:
    print(f'El precio del libro es ${precioLibro}')
elif 300 < cant_pagina < 600:
    print(f'${precioLibro} el precio del libro,\n+ ${tela} de la tela \n----------------- \nPrecio final: {precioLibro + tela}.  ')
elif cant_pagina > 600:
    print(f'${precioLibro} el precio del libro,\n+ ${tela} de la tela \n+ ${encuadernacion_especial} de la encuadernacion especial. ')

#Ejercicio 6
km = int(input('Ingrese la cantidad de kilometros: '))
viaje_minimo = 250
precio = 0

if 0 <= km < 10:
    precio = km * 30
    if precio <= 250:
        print(f'La tarifa es por el viaje mínimo: {viaje_minimo}')
    elif precio > 250:
        print(f'La tarifa es de: {precio}')
elif km >=10:
    precio = km * 20
    if precio <= 250:
        print(f'La tarifa es por el viaje mínimo: {viaje_minimo}')
    elif precio > 250:
        print(f'La tarifa es de: {precio}')

#Ejercicio 7
anio = int(input('Ingrese un año para saber si es bisiesto o no: '))
if anio % 4 == 0 and anio % 400 == 0:
    print('El año es bisiesto')
elif anio % 4 == 0:
    print('El año es bisiesto')
else:
    print('El año no es bisiesto')

#Ejercicio 8
dia = int(input('Ingrese un numero correspondiente a un dia: '))
mes = int(input('Ingrese un numero correspondiente a un mes: '))
anio = int(input('Ingrese un numero correspondiente a un año: '))
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
mes_selec = meses[mes-1]
if anio % 4 == 0 or anio % 400 == 0:
    if dia == 29 and meses[1]:
        print(f'{dia} de {mes_selec} del año {anio}')
    else:
        print(f'{dia} de {mes_selec} del año {anio}')
else:
    if dia >= 29 and meses[1]:
        print('La fecha es invalida, no hubo 29 de febrero ese año')
    else:
        print(f'{dia} de {mes_selec} del año {anio}')

#Ejercicio 9
sueldo_basico = int(input('Ingrese su sueldo basico: '))
antiguedad = int(input('Ingrese su antiguedad en años: '))
estado_civil = int(input('Ingrese su estado civil, ingrese 1 si esta soltero o 2 si es casado: '))
jubilacion = 0.11
obra_social = 0.03
sindicato = 0.03
sueldo_bruto = 0
sueldo_neto = 0
antiguedaad = 0
if estado_civil == 1:
    sueldo_bruto = sueldo_basico*(antiguedad * 1.05)
    antiguedaad = sueldo_basico * (antiguedad * 0.05)
elif estado_civil == 2:
    sueldo_bruto = sueldo_basico*(antiguedad * 1.07)
    antiguedaad = antiguedad * 1.07

sueldo_neto = sueldo_bruto - (sueldo_bruto * jubilacion) - (sueldo_bruto * obra_social) - (sueldo_bruto * sindicato)
print(f'Estado civil: {estado_civil}')
print(f'Sueldo básico: {sueldo_basico}')
print(f'Antiguedad: {antiguedaad}')
print(f'Descuentos:\nJubilacion: {sueldo_bruto * jubilacion}\nObra Social: {sueldo_bruto * obra_social}\nSindicato: {sueldo_bruto * sindicato}')
print(f'Sueldo neto: {sueldo_neto}')