#Precio con descuento
#Solicita el precio de un producto y el porcentaje de descuento. Calcula y muestra el descuento aplicado y el precio final.

precio=float(input("Ingrese el precio del producto: "))
descuento=float(input("Ingrese el porcentaje de descuento: "))
descuento_aplicado=precio*(descuento/100)

precio_final=precio-descuento_aplicado
print(f"El descuento de su producto es de: {descuento_aplicado} y el precio final es de: {precio_final}")