#Número par o impar
#Solicita un número entero. Determina si el número es par o impar y muestra el resultado.

numero=int(input("Ingrese un numero entero: "))

if numero%2==0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")