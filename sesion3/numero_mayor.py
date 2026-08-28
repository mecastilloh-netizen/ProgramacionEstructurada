#Mayor de tres números
#Solicita tres números enteros. Determina cuál es el mayor y muéstralo en pantalla.

num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercer numero: "))

if num1>num2 and num1>num3:
    print(f"El numero mayor es: {num1}")
elif num2>num1 and num2>num3:
    print(f"El numero mayor es: {num2}")
else:
    print(f"El numero mayor es: {num3}")