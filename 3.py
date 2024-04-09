num = int(input("Ingrese un numero por favor:"))


def tablas(numero):

    limite = 100
    count = 1
    while count <= limite:
        resultado = count * numero
        print(f"{numero} x {count} = {resultado}")
        count += 1


tablas(num)