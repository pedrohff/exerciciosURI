#Time limit exceeded
jogadas = []

def lerJogada(index, string):
    partes = string.split(" ")
    qtdPecas = int(partes[0])
    qtdTentativas = int(partes[1])
    pecas = []
    tentativas = []
    for i in range(0,qtdPecas):
        pecas.append(int(input()))
    for i in range(0,qtdTentativas):
        tentativas.append(int(input()))
    jogadas.append({
            'index': index,
            'pecas': pecas,
            'tentativas': tentativas
        })


index = 1
string = ""
while index <= 65 and (string != "0 0"):
    string = input()
    if(string != "0 0"):
        lerJogada(index, string)
    index+=1

for x in jogadas:
    print("CASE# %d:" %x['index'])
    for tentativa in x['tentativas']:
        if tentativa in x['pecas']:
            print("%d found at %d" % (tentativa, x['pecas'].index(tentativa)+2 ))
        else:
            print("%d not found" % tentativa)
