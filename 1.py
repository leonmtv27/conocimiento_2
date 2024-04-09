
def factor(x):
    if x < 0:
        raise ValueError("Recuerde que el factorial siempre es un número positivo")

    factor = 1
    for i in range(1,x+1):
        factor *= i
    return factor


number = int(input("Ingrese un número no negativo: "))
result = factor(number)
print(f"El factorial de {number} es {result}")