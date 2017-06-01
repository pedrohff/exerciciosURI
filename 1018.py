valor = int(input())
aux = valor

def calc(nota):
    global aux
    qtd = aux // nota
    if(qtd > 0):
        aux = aux - (qtd * nota)
    print("{0} nota(s) de R$ {1},00".format(qtd, nota))
    return qtd

print(valor)
calc(100)
calc(50)
calc(20)
calc(10)
calc(5)
calc(2)
calc(1)