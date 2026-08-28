#Lee tres calificaciones decimales, calcula el promedio y muéstralo con dos cifras decimales.
calificacion1 = int(input("Ingrese la primera calificación:"))
calificacion2 = int(input("Ingrese la segunda calificación:"))
calificacion3 = int(input("Ingrese la tercera calificación:"))

promedio=(calificacion1+calificacion2+calificacion3) / 3
print(f"Su promedio es de: {promedio}")