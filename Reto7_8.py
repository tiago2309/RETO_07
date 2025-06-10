import math

def exp_taylor(x, n):

    for i in range(n + 1):
        aproximacion += x**i / math.factorial(i)
        
    aproximacion = 0
    valor_real = math.exp(x)
    diferencia = abs(valor_real - aproximacion)
    return aproximacion, valor_real, diferencia

def main():
    # Solicita al usuario que ingrese los valores
    x = float(input("Ingrese el valor de x: "))
    n = int(input("Ingrese el número de términos n (entero positivo): "))
    
    aprox, real, diff = exp_taylor(x, n)
    
    print(f"\nAproximación de e^{x} con {n} términos: {aprox}")
    print(f"Valor real con math.exp({x}): {real}")
    print(f"Diferencia: {diff}")

# Ejecutar el programa
main()
