valores = [float(x) for x in input().split(" ")]
media = ( valores[0] * 2 + valores[1] * 3 + valores[2] * 4 + valores[3] * 1 )/10

print("Media: %.1f" %media)
if media >=7:
    print("Aluno aprovado.")
else:
    if media < 5 :
        print("Aluno reprovado.")
    else:
        print("Aluno em exame.")
        exame = float(input())
        print("Nota do exame: %.1f" % exame)
        final = (exame+media)/2
        print("Aluno aprovado.") if final > 5 else print("Aluno reprovado.")
        print("Media final: %.1f" % final)