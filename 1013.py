inputA = input()
valores = inputA.split(" ")

def maior(a,b):
    a = int(a) if type(a) is str else a
    b = int(b) if type(b) is str else b
    return a if a>b else b

ma = maior(valores[0],valores[1])
ma = maior(ma, valores[2])
print ("%d eh o maior" %ma)
