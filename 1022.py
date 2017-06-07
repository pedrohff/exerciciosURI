def soma(arrayIn):
    arrayOut = []
    arrayOut.append(arrayIn[0] * arrayIn[3] + arrayIn[2] * arrayIn[1])
    arrayOut.append(arrayIn[1] * arrayIn[3])
    return arrayOut

def sub(arrayIn):
    arrayOut = []
    arrayOut.append(arrayIn[0] * arrayIn[3] - arrayIn[2] * arrayIn[1])
    arrayOut.append(arrayIn[1] * arrayIn[3])
    return arrayOut

def mult(arrayIn):
    arrayOut = []
    arrayOut.append(arrayIn[0] * arrayIn[2])
    arrayOut.append(arrayIn[1] * arrayIn[3])
    return arrayOut

def div(arrayIn):
    arrayOut = []
    arrayOut.append(arrayIn[0] * arrayIn[3])
    arrayOut.append(arrayIn[1] * arrayIn[2])
    return arrayOut

def podeSimplificar(arrayIn, num):
    verificadorA = (arrayIn[0] % num == 0)
    verificadorB = (arrayIn[1] % num == 0)
    return verificadorA and verificadorB

def simplificador(arrayIn, num):
    arrayOut = []
    arrayOut.append(arrayIn[0] / num)
    arrayOut.append(arrayIn[1] / num)
    return arrayOut

def direcionaOperador(string, array):
    x = string[3]
    operadores = {
        '+': soma(array),
        '-': sub(array),
        '*': mult(array),
        '/': div(array)
    }
    return operadores.get(x)

def analisarString(string):
    caracteres = string.split(" ")
    numeros = string.replace("/", "")
    numeros = numeros.replace("+", "")
    numeros = numeros.replace("-", "")
    numeros = numeros.replace("*", "")

    #remove espaços em branco
    numeros = numeros.split(" ")

    #remove elementos nulos
    numeros = list(filter(None, numeros))

    #parse to int
    numeros = list(map(int,numeros))

    arrayResultado = direcionaOperador(caracteres, numeros)
    arraySimplificado = []
    menorNumero = abs(arrayResultado[0]) if (abs(arrayResultado[1]) > abs(arrayResultado[0])) else abs(arrayResultado[1])
    if(menorNumero > 0):
        for x in range(1,menorNumero+1):
            if(podeSimplificar(arrayResultado, x)):
                n = x
                arraySimplificado = simplificador(arrayResultado, x)
    else:
        arraySimplificado = arrayResultado

    print("%d/%d = %d/%d" % (arrayResultado[0], arrayResultado[1], arraySimplificado[0], arraySimplificado[1]))



repetidor = int(input())
entradas = []
for x in range(0,repetidor):
    entradas.append(input())

for i,string in enumerate(entradas):
    analisarString(string)