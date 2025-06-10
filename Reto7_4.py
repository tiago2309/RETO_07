def factorial(n):
    fac = 1
    for i in range (1, n + 1):
        fac *= i
    return fac

if __name__ == "__main__":
    n = int(input("Ingrese un numero natural: "))
    for i in range(1, n +1):
        print (f"{i}! = {factorial(i)}")