#Runtime error
import math
cidades = []
mediaCidades =[]
def lerCidade(qtdResidencias):
    residencias = []
    medias = {}
    for x in range(0,qtdResidencias):
        string = input()
        valores = string.split(" ")
        media = math.floor(int(valores[1]) / int(valores[0]))
        valoresResidencia = {
            'pessoas': int(valores[0]),
            'mediaConsumo': media,
            'consumo': int(valores[1])
        }
        if not media in medias:
            medias.update({
                media : int(valores[0])
            })
        else:
            medias[media] += int(valores[0])

        residencias.append(valoresResidencia)
    cidades.append(residencias)
    mediaCidades.append(medias)

def imprimirCidade(cidade, index):
    print("Cidade# %d:" %(index+1))
    mediaDaCidade = mediaCidades[index]
    medias = sorted(mediaCidades[index])

    string = ""
    for media in medias[:-1]:
        string += "%d-%d " % (mediaDaCidade[media], media)
    string += "%d-%d" %(mediaDaCidade[medias[-1]],medias[-1])
    print(string)

    totalPessoas = 0
    totalConsumo = 0
    aux = sorted(cidade, key= lambda c:c['mediaConsumo'])
    for residencia in aux:
        totalPessoas+= residencia['pessoas']
        totalConsumo+= residencia['consumo']
    print("Consumo medio: %.2f m3." %(totalConsumo/totalPessoas))

x = 999
while x != 0:
    x = int(input())
    lerCidade(x)

indexAuxiliar = 0
for index, cidade in enumerate(cidades[:-2]):
    # print(cidade)
    imprimirCidade(cidade, index)
    print()
    indexAuxiliar = index

if(len(cidades) > 2):
    imprimirCidade(cidades[-2], indexAuxiliar+1)
else:
    imprimirCidade(cidades[-2], indexAuxiliar)