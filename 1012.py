inputA = input()
string = inputA.split(" ")
A = float(string[0])
B = float(string[1])
C = float(string[2])

def triangulo():
    return A*C/2

def circulo():
    return 3.14159 * pow(C,2)

def trapezio():
    return ((A+B)*C)/2

def quadrado():
    return pow(B,2)

def retangulo():
    return A*B


print("TRIANGULO: %.3f" %triangulo())
print("CIRCULO: %.3f" %circulo())
print("TRAPEZIO: %.3f" %trapezio())
print("QUADRADO: %.3f" %quadrado())
print("RETANGULO: %.3f" %retangulo())