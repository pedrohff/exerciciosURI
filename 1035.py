i = input()
a = int(i.split(" ")[0])
b = int(i.split(" ")[1])
c = int(i.split(" ")[2])
d = int(i.split(" ")[3])

validacoes = []
validacoes.append(b > c)
validacoes.append(d > a)
validacoes.append(c+d > a+b)
validacoes.append(c>0 and d>0)
validacoes.append(a % 2 == 0)

verificador = True
for v in validacoes:
    verificador = verificador and v

print("Valores aceitos" if verificador else "Valores nao aceitos")