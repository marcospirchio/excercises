#Ejercicio 1
a = 12 * 4 + 4 * 5
print(a)
b = (12 * (1 - 5) + 4) * 3
print(b)
c = 12 * 1 - 5 + 4 * 3
print(c)
d = (17 - 2) / 5
print(d)
e = 3 + 2 * 2 - (8 * 4 + 1 / 2.0) * 3
print(e)
f = 5*4/ 2
print(f)
g = 5 * (4 / 2)
print(g)
h = 24 / 2 ** 2
print(h)
i = (24 / 2) ** 2
print(i)
j = 3+ 4*6/2 - 5
print(j)
k = 3 + 4 * 6 / (2-5)
print(k)
l = (- 0.1) * 3
print(l)
m = -9**2
print(m)
n = (-9)**2
print(n)
o = 10 / 3
print(o)
p = 10 // 3
print(p)
q = 10 // 3
print(q)

#Ejercicio 2
aa= int(input("ingrese un numero: "))
bb= int(input("ingrese un numero: "))
print(aa+bb)
print(aa-bb)

#Ejercicio 3
parcial1 = 9
parcial2 = 7
promedio = (parcial1 + parcial2) / 2
print(f'El promedio del alumno es: {promedio}')

#Ejercicio 4
edad = int(input("Ingresa tu edad: "))
edad_dias = edad * 365
print(f'La edad en dias es {edad_dias} dias')

#Ejercicio 5
inversion_total = 10000
inversion_marcos = 4500
inversion_colo = 3000
inversion_lucas = 2500
marcos = (inversion_marcos / inversion_total) * 100
colo = (inversion_colo / inversion_total) * 100
lucas = (inversion_lucas / inversion_total) * 100
print(f'En porcentajes, Marcos puso %{marcos}, el colo puso %{colo} y lucas puso %{lucas}')

#Ejercicio 6
num1 = int(input("Ingresa un numero : "))
num2 = int(input("Ingresa un numero : "))
num3 = int(input("Ingresa un numero : "))
promedio = (num1 + num2 + num3) / 3

#Ejercicio 7
dinero = int(input('cuanto dinero has invertido? '))
banco = 1.02
meses = 6
resultado = (dinero * meses) * banco
print(f'Has invertido {dinero} pesos, en {meses} meses, te han devuelto {resultado}')

#Ejercicio 8
metros = int(input('Ingrese una medida en metros: '))
cm = metros * 100
pulgada = cm / 2.54
pie = pulgada / 12
yarda = pie / 3
print(f'''Medida en metros {metros} 
medida en centimetros {cm}
medida en pulgadas {round(pulgada,5)}
medida en pies {round(pie,5)}
medida en yardas {round(yarda,5)}''')

#Ejercicio 9
vendedor = input('Ingrese su numero de vendedor: ')
ventas = int(input('Ingrese cuantas ventas realizo en el mes: '))
valor_ventas = int(input('ingrese el valor de las ventas del mes: '))
salario = 500000
comision = 5000
porcentaje = 0.05
salario_total = salario + comision * ventas + valor_ventas * porcentaje
print(f'Para el vendedor {vendedor}, el salario correspondiente a este mes es de: {salario_total}')

#Ejercicio 10
segundos = int(input('Ingrese una cantidad en segundos: '))
minutos = segundos / 60
horas = minutos / 60
dias = horas / 24
print(f'{segundos} segundos, {int(minutos)} minutos, {int(horas)} horas y {int(dias)} dias')

#Ejercicio 11
dinero1 = int(input('Ingrese la cantidad de dinero a retirar: '))
billetes1000 = 0
billetes500 = 0
billetes100 = 0
billetes50 = 0
billetes10 = 0
billetes5 = 0
billetes1 = 0
while dinero1 >= 1000:
    billetes1000 += 1
    dinero1 -= 1000
while dinero1 >= 500:
    billetes500 +=1
    dinero1 -= 500
while dinero1 >= 100:
    billetes100 += 1
    dinero1 -= 100
while dinero1 >= 50:
    billetes50 += 1
    dinero1 -= 50
while dinero1 >= 10:
    billetes10 += 1
    dinero1 -= 10
while dinero1 >= 5:
    billetes5 += 1
    dinero1 -= 5
while dinero1 >= 1:
    billetes1 += 1
    dinero1 -= 1
print(f'el banco pagara con: \n{billetes1000} billetes de $1000\n{billetes500} billetes de $500\n{billetes100} billetes de $100\n{billetes50} billetes de $50\n{billetes10} billetes de $10\n{billetes5} billetes de $5\n{billetes1} billetes de $1')

#Ejercicio 12
----