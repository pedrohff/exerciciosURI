from decimal import Decimal, ROUND_HALF_UP
valor = float(input())
aux = valor

def calc(nota):
    global aux
    qtd = aux // nota
    if(qtd > 0):
        aux = aux - (qtd * nota)

    print("%d nota(s) de R$ %d.00"%(qtd, nota))
    return qtd

def calcMoeda(nota):
    global aux
    if(aux > 0.05):
        qtd = aux // nota
    else:
        x = Decimal( Decimal(str(aux)).quantize(Decimal('1.11'), rounding=ROUND_HALF_UP) )
        # print(x)
        nota = Decimal(str(nota))
        # print(nota)
        qtd = x // nota
        # print(qtd)
    if(qtd > 0 and aux > 0.05):
        aux = aux - (qtd * nota)

    print("%d moeda(s) de R$ %.2f"%(qtd, nota))
    return qtd

print("NOTAS:")
calc(100)
calc(50)
calc(20)
calc(10)
calc(5)
calc(2)

print("MOEDAS:")
calcMoeda(1.00)
calcMoeda(0.50)
calcMoeda(0.25)
calcMoeda(0.10)
calcMoeda(0.05)
calcMoeda(0.01)
