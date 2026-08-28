#Leer tres numeros y evualuar logicamente
number1 = int(input("Leer el primer valor: "))
number2 = int(input("Leer el segundo valor: "))
number3 = int(input("Leer el tercer valor: "))

#Evaluar que numero1 sea mayor a mayor2 y numero1 mayor a numero3
print("Respuesta 1")
print(f"({number1} > {number2}) Y ({number1} > {number3}) : {number1 > number2 and number1 > number3} ")


#Evaluar que numero1 sea mayor o igual a numero3 y numero3 menor que numero2
print("Respuesta 2")
print(f"({number1} >= {number3}) o ({number3} < {number2}) : {number1 >= number3 or number3 < number2}")

#Negar que numero1 sea mayor que numero2
print("Respuesta 3")
print(f"(No es: {number1} > {number2}) : {not(number1 > number2)}")

#Asignacion
number1 = 16
number1 += 14
number1 -= number2
print(f"numero 1: {number1}")