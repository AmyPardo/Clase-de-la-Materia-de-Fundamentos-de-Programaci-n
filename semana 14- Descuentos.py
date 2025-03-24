precio = (float(input("Ingrese el precio del producto: ")))

def producto_descuento (precio, descuento=10):
    descuento1 = precio * (descuento/100)
    return (descuento1)

descuento_final = producto_descuento (precio)
print ("Su descuento es del 10%")

valor_final = (precio - descuento_final)
print ("Su valor final a pagar aplicando el 10% de descuento es de:", valor_final)