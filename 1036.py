from math import sqrt

input = input()
valores = [float(x) for x in input.split(" ")]
a = valores[0]
b = valores[1]
c = valores[2]

def delta(a,b,c):
    return pow(b,2) - (4*a*c)

def bhaskaraPos (a,b,c):
    return ( (-b) + sqrt(delta(a,b,c)) ) / (2*a)

def bhaskaraNeg (a,b,c):
    return ( (-b) - sqrt(delta(a,b,c)) ) / (2*a)

if(a != 0 and delta(a,b,c) > 0):
    print("R1 = %.5f" % bhaskaraPos(a,b,c))
    print("R2 = %.5f" % bhaskaraNeg(a,b,c))
else:
    print("Impossivel calcular")