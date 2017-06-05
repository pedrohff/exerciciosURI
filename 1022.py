def soma(arrayIn):
    arrayOut = []
    arrayOut[0] = arrayIn[0] * arrayIn[3] + arrayIn[2] * arrayIn[1]
    arrayOut[1] = arrayIn[1] * arrayIn[3]
    return arrayOut

def podeSimplificar(arrayIn, num):
    verificadorA = (arrayIn[0] % num == 0)
    verificadorB = (arrayIn[1] % num == 0)
    return verificadorA and verificadorB

def simplificador(arrayIn, num):
    arrayOut = []
    arrayOut[0] = arrayIn[0] / 2
    arrayOut[1] = arrayIn[1] /2
    return arrayOut

def arrayToInt(array):
    for x in array:
        print(x)
        x = int(x)

def analisarString(string):
    caracteres = string.split(" ")
    numeros = string.replace("/", "")
    numeros = numeros.replace("+", "")
    numeros = numeros.replace("-", "")
    numeros = numeros.replace("*", "")
    numeros = numeros.split(" ")
    numeros = list(filter(None, numeros))
    numeros = arrayToInt(numeros)
    print(numeros)
    if(caracteres[3] == "+"):
        arraySoma = soma(numeros)
        if(podeSimplificar(arraySoma, 2)):
            return simplificador(arraySoma, 2)


string = input()
resultado = analisarString(string)
print("%d / %d" %(resultado[0], resultado[1]) )
