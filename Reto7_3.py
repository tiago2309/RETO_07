def pares_descendentes(n):
    if n % 2 != 0:
        n -= 1
    while n >= 2:
        print (n)
        n -= 2

if __name__ == "__main__":
    n = int(input("Ingrese un numero mayor o igual a 2: "))
    pares_descendentes(n) 