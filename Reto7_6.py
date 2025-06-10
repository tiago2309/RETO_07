n = int(input("Ingrese un numero natural: "))
x = float(input("Ingrese un numero real: "))

if n > 0:
    resultado = 1
    for _ in range(n):
        resultado *= x
    
    print(f"{x} elevado a la {n} es: {resultado}")

