def potencia_dos(n):
    resultado = 1
    for _ in range(n):
        resultado *= 2
    return resultado


if __name__ == "__main__":
    n = int(input("Ingrese un número natural: "))
    print(f"2^{n} = {potencia_dos(n)}")