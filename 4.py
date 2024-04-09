def iva(productos):
    for producto in productos:
        precio = float(input(f"Ingrese el precio del producto {producto}: "))
        con_iva = (precio * 0.19) + precio
        print(f"El precio con IVA para {producto} es: {con_iva:.2f}")
        print(f"El precio sin IVA para {producto} es: {precio:.2f}")

productos = []
for i in range(10):
    nombre_producto = input(f"Ingrese el nombre del producto {i + 1}: ")
    productos.append(nombre_producto)

iva(productos)