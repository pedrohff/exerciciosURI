strings = []
def passoum(str):
    string = ""
    for x in str:
        if(x.isalpha()):
            char = ord(x)+3
            string+= chr(char)
        else:
            string+=x
    return string

def passotres(str):
    l = len(str)
    um = str[0:int((l/2))]
    dois = str[int((l/2)):l]
    tres = ""
    for char in dois:
        char = chr( ord(char)-1 )
        tres+=char

    return um+tres

def criptografia(str):
    str = passoum(str)
    str = str[::-1]
    str = passotres(str)
    print(str)


qtd = int(input())
codigos = []
for x in range(0,qtd):
    codigos.append(input())

for codigo in codigos:
    criptografia(codigo)