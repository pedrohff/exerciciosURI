valor = float(input())

intervalo = ""

if(valor >= 0 and valor <= 25):
    intervalo="[0,25]"

if (valor > 25 and valor <= 50):
    intervalo = "(25,50]"

if(valor > 50 and valor <= 75):
    intervalo="(50,75]"

if (valor > 75 and valor <= 100):
    intervalo = "(75,100]"

x = "Intervalo %s" %intervalo if intervalo != "" else "Fora de intervalo"

print(x)