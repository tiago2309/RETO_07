def numeros_pares():
    n = 2
    while n <= 1000:
        print (n)
        n += 2

def numeros_impares():
    n = 1
    while n <= 1000:
        print (n)
        n += 2

if __name__ == "__main__":
    print ("Pares del 1 al 1000")
    numeros_pares()

    print ("Impares del 1 al 1000")
    numeros_impares()
