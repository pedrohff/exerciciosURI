a = input()
b = input()

a = a.split(" ")
b = b.split(" ")


def multString(a):
    return float(a[1]) * float(a[2])

resultado = multString(a) + multString(b)

print("VALOR A PAGAR: R$ %.2f" %resultado)